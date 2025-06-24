# 🎬 Movie Recommendation System (Content-Based + Streamlit + TMDB API)

An intelligent **Movie Recommendation System** that suggests similar movies using metadata (genres, cast, director, keywords) with **content-based filtering**, **cosine similarity**, and an interactive **Streamlit UI**. It also integrates with the **TMDB API** to fetch movie **posters and visuals** dynamically for a richer user experience.

---

## 🚀 Features

- 📽️ Recommends similar movies based on content metadata
- 💡 Uses **CountVectorizer** + **Cosine Similarity**
- 🌐 Clean and interactive Streamlit frontend
- 🖼️ Dynamically fetches movie posters using **TMDB API**
- 🔎 Fast and offline search with optional real-time visual enrichment

---

## 🧠 How It Works

1. **Data Preprocessing**:
   - Merge movie metadata with credits and keywords
   - Extract relevant features: genres, keywords, cast, director

2. **Content-Based Filtering**:
   - Combine features into a single string and preprocess them using **Spacy**
   - Apply **CountVectorizer** to convert text to numeric format
   - Compute **Cosine Similarity** between movie vectors

3. **Recommendation Engine**:
   - Take a movie title as input
   - Return top N most similar movies using cosine similarity scores

4. **TMDB API Integration**:
   - Fetch poster images based on movie ID
   - Display posters using Streamlit

---

## 🧰 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit (Frontend)
- TMDB API (for Posters)

---

## 📂 Dataset

- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Files Used:
  - `movies_metadata.csv`
  - `credits.csv`
