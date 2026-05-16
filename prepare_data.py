import pandas as pd
import os

def prepare():
    input_path = "data/musiccaps-public.csv"
    output_path = "data/processed_music.csv"

    if not os.path.exists(input_path):
        print("Error: music_caps.csv not found! Check your data folder.")
        return

    # Load the Kaggle data
    df = pd.read_csv(input_path)
    
    # We keep 'ytid' for playback and 'caption' for the NLP engine
    clean_df = df[['ytid', 'caption']]
    
    # Save the cleaned version
    clean_df.to_csv(output_path, index=False)
    print(f"--- SUCCESS ---")
    print(f"Processed {len(clean_df)} songs.")
    print(f"Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    prepare()