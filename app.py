from flask import Flask, render_template, request
import pandas as pd
import faiss
import torch
import lyricsgenius
import yt_dlp
import numpy as np
from engine import VibeEngine

app = Flask(__name__)
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("genius")
# Load everything once at startup
engine = VibeEngine()
index = faiss.read_index("data/music_vibes.index")
df = pd.read_csv("data/processed_music.csv")

def get_lyrics(ytid):
    ydl_opts = {'quiet': True, 'no_warnings': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={ytid}", download=False)
            raw_title = info.get('title', '')
            
            # CLEANING: Remove common YouTube noise that confuses the Lyrics API
            clean_title = raw_title.split('(')[0].split('[')[0].split('|')[0]
            clean_title = clean_title.replace('Official Video', '').replace('Official Audio', '').strip()
            
            print(f"Searching Genius for cleaned title: {clean_title}")
            song = genius.search_song(clean_title)
            return song.lyrics if song else "Lyrics not found for this track."
        except Exception as e:
            print(f"Error: {e}")
            return "Could not fetch metadata or lyrics."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('vibe_query')
    
    # 1. AI Vector Search
    query_vec = engine.get_text_vibe(query)
    if not torch.is_tensor(query_vec): query_vec = query_vec[0]
    query_np = query_vec.detach().cpu().numpy().reshape(1, -1).astype('float32')
    faiss.normalize_L2(query_np)
    
    _, indices = index.search(query_np, 1)
    match_idx = indices[0][0]
    
    # 2. Get Data
    yt_id = df.iloc[match_idx]['ytid']
    vibe_desc = df.iloc[match_idx]['caption']
    
    # 3. Get Exact Lyrics
    lyrics = get_lyrics(yt_id)
    # Change this in your search function
    distances, indices = index.search(query_np, 1)
    confidence = float(distances[0][0]) * 100  # Convert to a percentage

    return render_template('index.html', 
                       query=query, 
                       yt_id=yt_id, 
                       vibe=vibe_desc, 
                       lyrics=lyrics,
                       confidence=round(confidence, 2))

if __name__ == '__main__':
    app.run(debug=True)