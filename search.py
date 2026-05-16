import pandas as pd
import faiss
import numpy as np
import torch
import lyricsgenius
import yt_dlp
from engine import VibeEngine
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GENIUS_TOKEN")
# 1. Setup Genius (Paste your Token here)

def get_video_title(youtube_id):
    """Uses yt-dlp to get the actual song title from the YouTube link."""
    ydl_opts = {'quiet': True, 'no_warnings': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={youtube_id}", download=False)
            return info.get('title', None)
        except:
            return None

def search_vibe(query_text, top_k=1): # top_k=1 to focus on the best match for lyrics
    engine = VibeEngine()
    df = pd.read_csv("data/processed_music.csv")
    index = faiss.read_index("data/music_vibes.index")
    
    print(f"\nSearching for vibe: '{query_text}'...")
    
    # NLP Vector Conversion
    query_vec = engine.get_text_vibe(query_text)
    if not torch.is_tensor(query_vec):
        query_vec = query_vec[0]
        
    query_numpy = query_vec.detach().cpu().numpy().reshape(1, -1).astype('float32')
    faiss.normalize_L2(query_numpy)
    
    # Vector Search
    distances, indices = index.search(query_numpy, top_k)
    
    print("\n--- BEST MATCH FOUND ---")
    idx = indices[0][0]
    youtube_id = df.iloc[idx]['ytid']
    
    # STEP 1: Get Song Title from YouTube
    print("Extracting song metadata from YouTube...")
    full_title = get_video_title(youtube_id)
    print(f"Detected Song: {full_title}")
    
    # STEP 2: Fetch Exact Lyrics from Genius
    if full_title:
        print("Fetching exact lyrics from Genius database...")
        # Clean the title a bit (remove 'Official Video' etc. for better matching)
        clean_title = full_title.split('(')[0].split('[')[0]
        song = genius.search_song(clean_title)
        
        if song:
            print("\n================ EXACT LYRICS ================")
            print(song.lyrics[:1500]) # Shows first 1500 characters
            print("==============================================")
        else:
            print("Match found, but exact lyrics were not found on Genius.")
    
    print(f"\nListen here: https://www.youtube.com/watch?v={youtube_id}")

if __name__ == "__main__":
    user_query = input("Enter a vibe to search for: ")
    search_vibe(user_query)