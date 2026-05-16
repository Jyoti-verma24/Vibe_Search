# VibeSearch 🎵

AI-powered semantic music recommendation system that finds songs based on **mood, emotion, and vibe** instead of exact song names or keywords.

Users can enter natural language prompts like:

- `"late night lonely feeling"`
- `"songs for long night drive"`
- `"rain + coffee + overthinking vibe"`

The system intelligently recommends the most relevant songs using **NLP embeddings + vector similarity search**.

---

# 🚀 Features

- 🎧 Semantic vibe-based music search
- 🧠 NLP-powered emotion understanding
- ⚡ Fast similarity search using FAISS
- 🎵 Automatic YouTube song detection
- 📜 Lyrics fetching using Genius API
- 🔍 Embedding-based recommendation engine
- 🌐 Simple Flask web interface

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask

## AI / NLP
- Sentence Transformers
- PyTorch
- FAISS

## APIs & Libraries
- lyricsgenius
- yt-dlp
- pandas
- numpy

---

# 📂 Project Structure

```plaintext
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
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/VibeSearch.git
cd VibeSearch
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv vibesearch_env
```

### Activate Environment

### Windows

```bash
vibesearch_env\Scripts\activate
```

### Mac/Linux

```bash
source vibesearch_env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
GENIUS_TOKEN=your_api_key_here
```

---

# ▶️ Run The Project

```bash
python app.py
```

Open in browser:

```plaintext
http://127.0.0.1:5000
```

---

# 🧠 How It Works

1. User enters a mood or vibe query
2. Query is converted into embeddings
3. FAISS searches similar vectors
4. Best matching song is retrieved
5. YouTube metadata is extracted
6. Lyrics are fetched using Genius API

---

# 💡 Example Queries

```text
late night lonely feeling
```

```text
songs for coding at midnight
```

```text
rainy evening calm vibes
```

```text
songs that feel nostalgic
```

```text
main character energy songs
```

---

# 🔒 Security

Sensitive files are excluded using `.gitignore`:

- `.env`
- `kaggle.json`
- `vibesearch_env`

---

# 📌 Future Improvements

- Spotify API integration
- Playlist generation
- Voice emotion detection
- Real-time recommendations
- Mobile responsive UI
- Multi-language support
