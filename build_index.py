import pandas as pd
import numpy as np
import faiss
import torch
from engine import VibeEngine

def build():
    # 1. Load the cleaned data
    # Make sure this matches the file created by prepare_data.py
    df = pd.read_csv("data/processed_music.csv")
    engine = VibeEngine()
    
    # We will start with the first 500 songs for a solid test
    num_samples = min(5000, len(df)) 
    print(f"Creating embeddings for {num_samples} songs... (This uses the NLP Engine)")
    
    captions = df['caption'].head(num_samples).tolist()
    
    vectors = []
    for i, text in enumerate(captions):
        if i % 50 == 0: 
            print(f"Processing: {i}/{num_samples}")
            
        vec = engine.get_text_vibe(text)
        
        # If 'vec' is still the 'BaseModelOutput' object, we force it to a tensor
        if not torch.is_tensor(vec):
            # This is the 'brute force' way to grab the first tensor inside the object
            vec = vec[0] 
        
        # Now conversion will work 100%
        numpy_vec = vec.detach().cpu().numpy().reshape(1, -1)
        vectors.append(numpy_vec)
    
    # 2. Setup FAISS (The Vector Database)
    vector_matrix = np.vstack(vectors).astype('float32')
    dimension = 512 # The size of a CLAP vector
    
    # IndexFlatIP uses 'Inner Product' which is Cosine Similarity for normalized vectors
    index = faiss.IndexFlatIP(dimension) 
    faiss.normalize_L2(vector_matrix) # Crucial for accurate 'vibe' matching
    index.add(vector_matrix)
    
    # 3. Save the Index
    faiss.write_index(index, "data/music_vibes.index")
    print("--- SUCCESS ---")
    print("Search index saved to data/music_vibes.index")

if __name__ == "__main__":
    build()