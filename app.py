import streamlit as st
import numpy as np
import pandas as pd
import requests

# ------------------------
# ENTER YOUR TMDB API KEY HERE
# ------------------------
TMDB_API_KEY = "37096edb848bd61c4b069c7003beaba6"

st.set_page_config(page_title="CineXplain 🎬 Movie Recommender 🎞️", layout="wide")

# ------------------------
# Load compressed AI movie data
# ------------------------
@st.cache_data
def load_data():
    data = np.load("movie_data.npz", allow_pickle=True)
    return data["titles"], data["movie_ids"], data["similarity"]

titles, movie_ids, similarity = load_data()
titles = titles.tolist()

# ------------------------
# TMDB Poster Fetcher
# ------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    try:
        response = requests.get(url).json()
        poster_path = response.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

# ------------------------
# Movie Recommendation Engine
# ------------------------
def recommend(movie_name):
    idx = titles.index(movie_name)
    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    rec_titles = []
    rec_posters = []

    for i in movie_list:
        rec_titles.append(titles[i[0]])
        rec_posters.append(fetch_poster(movie_ids[i[0]]))

    return rec_titles, rec_posters

# ------------------------
# UI CSS
# ------------------------
st.markdown("""
<style>
.header {
    padding: 20px;
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #ff002f, #ff8a00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.movie-card {
    border-radius: 15px;
    padding: 10px;
    background: rgba(255,255,255,0.07);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.15);
    transition: 0.25s;
}
.movie-card:hover {
    transform: scale(1.08);
    box-shadow: 0px 0px 25px rgba(255,0,50,0.7);
}

.movie-title {
    color: white;
    text-align: center;
    font-size: 16px;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# UI Header
# ------------------------
st.markdown("<div class='header'>CineXplain 🎬 Movie Recommender 🎞️</div>", unsafe_allow_html=True)

# ------------------------
# Movie selector
# ------------------------
selected_movie = st.selectbox("Choose a movie:", titles)

# Storage variables
rec_titles = None
rec_posters = None

if st.button("Show Recommendations"):
    rec_titles, rec_posters = recommend(selected_movie)
    st.subheader(f"Recommendations for {selected_movie}")

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"<div class='movie-card'>"
                f"<img src='{rec_posters[i]}' width='100%'>"
                f"<div class='movie-title'>{rec_titles[i]}</div>"
                f"</div>",
                unsafe_allow_html=True
            )