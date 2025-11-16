import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests
import os

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(
    page_title="NETSERVE Movie Recommender",
    layout="wide",
    page_icon="🎬"
)

# -------------------------------
# CUSTOM CSS + UI ANIMATIONS
# -------------------------------
st.markdown("""
<style>

body {
    background-color: #0d0f12;
}

.header {
    background: linear-gradient(90deg, #7a0000, #b30000);
    padding: 25px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 0px 20px #ff000020;
}

.header h1 {
    color: white;
    font-size: 45px;
    font-weight: 900;
    text-shadow: 2px 2px 6px black;
}

.movie-card {
    transition: all 0.3s ease;
    cursor: pointer;
    padding: 10px;
}

.movie-card:hover {
    transform: scale(1.08);
}

.poster {
    border-radius: 10px;
    box-shadow: 0px 0px 12px #00000070;
}

.movie-title {
    margin-top: 10px;
    color: white;
    font-weight: 600;
    font-size: 18px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD MOVIE DATA
# -------------------------------
@st.cache_resource
def load_data():
    data = np.load("movie_data.npz", allow_pickle=True)
    movies = pd.DataFrame(data["movies"], columns=["movie_id", "title"])
    similarity = data["similarity"]
    return movies, similarity

movies, similarity = load_data()

# -------------------------------
# TMDB API KEY (FROM STREAMLIT SECRETS)
# -------------------------------
TMDB_KEY = st.secrets["37096edb848bd61c4b069c7003beaba6"]

# -------------------------------
# POSTER FETCHER
# -------------------------------
def get_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_KEY}&language=en-US"
        response = requests.get(url).json()
        poster_path = response.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# -------------------------------
# RECOMMEND FUNCTION
# -------------------------------
def recommend(movie_title):
    index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendations.append(movies.iloc[i[0]].title)
        posters.append(get_poster(movie_id))

    return recommendations, posters

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<div class="header">
    <h1>NETSERVE Movie Recommender System 🎬</h1>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INPUT UI
# -------------------------------
movie_name = st.selectbox(
    "Choose a movie to recommend:",
    movies["title"].astype(str).tolist()
)

if st.button("Show Recommendation"):
    with st.spinner("🔍 Fetching recommendations..."):
        names, posters = recommend(movie_name)

    st.subheader(f"Recommendations for {movie_name}")

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div class="movie-card">
                    <img src="{posters[i]}" class="poster" width="200">
                    <div class="movie-title">{names[i]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )