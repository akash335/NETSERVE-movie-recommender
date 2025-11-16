# 🎬 CineXplain Movie Recommender 🎞️

A movie recommendation system using content-based similarity, deployed using Streamlit with TMDB API integration.

# Project Overview
CineXplain is a movie recommendation web app that helps users discover similar movies based on a chosen title. It analyzes movie metadata (genres, keywords, overview) and uses NLP + cosine similarity to recommend the most relevant movies.

This project includes:
✅ Data processing
✅ Feature extraction
✅ Similarity computation
✅ TMDB poster fetching
✅ Modern UI with animations + custom CSS
✅ Streamlit Cloud deployment

# 👨‍💻 Team Members
| Name              | Roll Number |
| ----------------- | ----------- |
| Porumamilla Akash | 12341590    |
| Kammari Amandeeip | 12341060    |
| Gangadhar         | 12340860    |


# AI Concepts Used
Vector Space Model
Text Processing (TF-IDF / Bag-of-Words)
Feature Engineering
Cosine Similarity
Search-based Recommendation
State Space Representation
Problem Reduction
Automated Reasoning Concepts

# Dataset
We used TMDB’s publicly available dataset:

tmdb_5000_movies.csv
tmdb_5000_credits.csv

Both files are merged and processed into a compressed movie_data.npz.

# How it Works
1. All movie genres, keywords, and descriptions are combined into a single text “tag”.
2. Tags are converted into vectors.
3. Cosine similarity calculates how close movies are.
4. TMDB API fetches posters dynamically.
5. Streamlit presents results in an animated UI.

# 🔐 TMDB API
Add your API key inside app.py: TMDB_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Running Locally
pip install -r requirements.txt
python build_npz.py
streamlit run app.py

# Live Demo
🔗 https://cinexplain-movie-recommender.streamlit.app/