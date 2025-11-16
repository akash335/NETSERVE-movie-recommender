🎬 CineXplain – Movie Recommender System 🎞️

# 👨‍💻 Team Members
| Name              | Roll Number |
| ----------------- | ----------- |
| Porumamilla Akash | 12341590    |
| Kammari Amandeeip | 12341060    |
| Gangadhar         | 12340860    |

# Project Overview
* CineXplain is a movie recommender system that uses content-based similarity search to suggest movies.
* The system uses vector representations, search algorithms, and probabilistic reasoning concepts to compute the closest recommendations.
* We also designed a modern, interactive UI using Streamlit, making the system visually appealing and highly user-friendly.

# Concepts Used
1. Problem Solving by Search

* Every movie is treated as a state.
* Recommendation = finding the closest state in the movie space.
* We use a similarity graph where nodes = movies and edges = similarity weights.
* Recommendation = graph search using cosine similarity (heuristic-based best-first retrieval).

2. State Space Representation

* Each movie → represented as a feature vector using:
   --> Overview text
   --> Genres
   --> Keywords
* These form a multi-dimensional state space.

3. Constraint Satisfaction

* Only movies satisfying constraints are recommended:
   --> Same language
   --> Similar genres
   --> Relevant keywords
* This follows CSP filtering to eliminate irrelevant states.

4. Automated Reasoning & Knowledge-Based Systems

* The system constructs a knowledge base from:
   --> TMDB movies dataset
   --> Metadata (keywords, genres, descriptions)
* Movie similarity is inferred using reasoning rules:
   --> “Movies sharing many keywords are likely similar.”
   --> “Movies with related genre vectors have higher similarity.”

5. Logical Inference

* Text processing uses:
   --> Basic first-order logic-like reasoning
   --> Feature extraction → logical attributes
   --> Deduction: selecting movies satisfying similarity conditions

6. Planning Algorithms (High-Level)

* Recommending a movie is equivalent to planning a next step in the user's preference sequence.
* System uses partial-order planning:
   --> Match movie metadata
   --> Retrieve similar movies
   --> Rank using heuristic score

7. Probabilistic Reasoning

* Recommendations approximate a probabilistic belief:
   --> Higher similarity → higher probability of relevance
* Similarity scores act like probabilistic weights.

8. Belief Networks (Conceptual Use)

* Although not explicitly built, the similarity network behaves like a belief graph:
   --> Nodes influence each other's relevance
   --> Similar movies propagate probability mass

9. Fuzzy Logic

* Genre and keyword matches are not binary.
* Partial overlap → partial membership
* “Similarity” is computed using fuzzy membership functions.

10. Reinforcement Learning (Conceptual Tie-In)

* The system “prefers” movies that historically correlate strongly.
* This resembles:
   --> Policy search
   --> Reward = similarity score

11. Applications

* Personalized entertainment recommendations
* OTT platform
Content discovery systems

Marketing analytics

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