import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading CSV files...")

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# credits movie_id → id for merging
credits = credits.rename(columns={"movie_id": "id"})

print("Merging data...")
movies = movies.merge(credits, on="id")

# After merge we now have: title_x (real title), title_y (credits)
movies = movies.rename(columns={
    "title_x": "title",
})

# remove credits title
if "title_y" in movies.columns:
    movies = movies.drop(columns=["title_y"])

# Clean genres + keywords
def extract_names(x):
    try:
        items = ast.literal_eval(x)
        return " ".join(i["name"] for i in items)
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

print("Saving compressed movie_data.npz ...")
np.savez_compressed(
    "movie_data.npz",
    movie_ids=movies["id"].values,
    titles=movies["title"].values,
    similarity=similarity
)

print("DONE! movie_data.npz generated successfully.")
