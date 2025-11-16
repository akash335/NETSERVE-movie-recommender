import streamlit as st
import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="NETSERVE Movie Recommender", layout="wide")

@st.cache_resource
def load_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")

    credits.rename(columns={"movie_id": "id"}, inplace=True)
    movies = movies.merge(credits, on="id")

    def extract_names(x):
        try:
            arr = ast.literal_eval(x)
            return " ".join([d["name"] for d in arr])
        except:
            return ""

    movies["genres"] = movies["genres"].apply(extract_names)
    movies["keywords"] = movies["keywords"].apply(extract_names)

    movies["overview"] = movies["overview"].fillna("")
    movies["tags"] = (
        movies["overview"] + " " +
        movies["genres"] + " " +
        movies["keywords"]
    )

    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies["tags"]).toarray()
    similarity = cosine_similarity(vectors)

    return movies, similarity

movies, similarity = load_data()

# Header UI
st.markdown("""
<div style='background:#7a0000;padding:20px;border-radius:10px;color:white;font-size:32px;font-weight:bold;'>
NETSERVE Movie Recommender System 🎬
</div>
""", unsafe_allow_html=True)

# Movie selector
movie_list = movies["title_x"].values
selected = st.selectbox("Choose a movie to recommend:", movie_list)

# Recommendation function
def recommend(movie):
    idx = movies[movies["title_x"] == movie].index[0]
    distances = similarity[idx]
    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return movies.iloc[[i[0] for i in movie_indices]]

# Button
if st.button("Show Recommendation"):
    results = recommend(selected)

    st.subheader(f"Recommendations for **{selected}**")

    cols = st.columns(5)
    for idx, row in enumerate(results.itertuples()):
        with cols[idx]:
            st.write(row.title_x)
            st.image(f"https://image.tmdb.org/t/p/w500{movies.iloc[row.Index].get('poster_path','')}",
                     use_container_width=True)
