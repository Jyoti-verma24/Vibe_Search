VibeSearch 🎵

AI-powered semantic music recommendation system that finds songs based on mood, emotion, and vibe instead of exact song names or keywords.

Users can enter natural language prompts like:

"late night lonely feeling"
"songs for long night drive"
"rain + coffee + overthinking vibe"

and the system intelligently recommends the most relevant music using NLP embeddings + vector similarity search.

🚀 Features
🎧 Semantic vibe-based music search
🧠 NLP-powered understanding of emotions and moods
⚡ Fast similarity search using FAISS
🎵 Automatic YouTube song detection
📜 Lyrics fetching using Genius API
🔍 Embedding-based recommendation engine
🌐 Simple web interface using Flask

🛠️ Tech Stack
Backend
Python
Flask
AI / NLP
Sentence Transformers
PyTorch
FAISS
APIs & Libraries
Genius API (lyricsgenius)
yt-dlp
pandas
numpy


📂 Project Structure
VIBESEARCH/
│
├── data/
│   ├── music_vibes.index
│   ├── processed_music.csv
│   ├── musiccaps-public.csv
│   └── kaggle.json
│
├── templates/
│   └── index.html
│
├── app.py
├── search.py
├── engine.py
├── prepare_data.py
├── build_index.py
├── .env
├── .gitignore
└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/VibeSearch.git
cd VibeSearch
2️⃣ Create Virtual Environment
python -m venv vibesearch_env

Activate environment:

Windows
vibesearch_env\Scripts\activate
Mac/Linux
source vibesearch_env/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root folder:

GENIUS_TOKEN=your_genius_api_key
▶️ Run the Project
Run Flask App
python app.py

Then open:

http://127.0.0.1:5000

🧠 How It Works
User enters a mood or vibe query.
The query is converted into vector embeddings using NLP models.
FAISS performs similarity search on stored music embeddings.
Best matching song is retrieved.
YouTube metadata is extracted.
Lyrics are fetched using Genius API.

📸 Example Queries
late night lonely feeling
music for coding at midnight
rainy evening calm vibes
songs that feel nostalgic
main character energy songs

🔒 Security

Sensitive files are excluded using .gitignore:

.env
kaggle.json
vibesearch_env

📌 Future Improvements
Spotify API integration
Playlist generation
Emotion detection from voice
Real-time recommendation system
Mobile responsive UI
Multi-language support
