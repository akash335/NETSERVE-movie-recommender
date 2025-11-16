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

8. Fuzzy Logic

* Genre and keyword matches are not binary.
* Partial overlap → partial membership
* “Similarity” is computed using fuzzy membership functions.

9. Reinforcement Learning (Conceptual Tie-In)

* The system “prefers” movies that historically correlate strongly.
* This resembles:
   --> Policy search
   --> Reward = similarity score

10. Applications

* Personalized entertainment recommendations
* OTT platforms
* Content discovery systems
* Marketing analytics

# Features
1. Content-based recommendation using AI
2. Cosine Similarity matrix from movie metadata
3. TMDB API integration for posters
4. Fully responsive UI with animations
5. Fast search using NumPy vectors
6. Modern black & neon themed interface

# Tech Stack
* Python
* Pandas, NumPy, Scikit-learn
* Streamlit UI
* TMDB API
* CSS animations

# Dataset
We used TMDB’s publicly available dataset:

tmdb_5000_movies.csv
tmdb_5000_credits.csv

Both files are merged and processed into a compressed movie_data.npz.

# How it Works
1. Tags Creation (Knowledge Representation)
   --> All movie genres, keywords, and overview descriptions are merged into one combined text field called a “tag”, forming a unified knowledge representation of each movie.

2. Vectorization (State-Space Encoding)
   --> Each movie tag is converted into a numerical feature vector, representing the movie in a high-dimensional state space using NLP techniques.

3. Similarity Computation (Heuristic Search)
   --> Using cosine similarity, the system calculates how “close” two movies are.
   --> Higher similarity = movies share themes, genres, and content.

4. Poster Retrieval (External Knowledge Access)
   --> For each recommended movie, the TMDB API is used to fetch the official poster image dynamically using the movie’s TMDB ID.

5. Interactive UI Output (AI Application Layer)
   --> A modern Streamlit interface displays recommendations with animated movie cards, smooth hover effects, and a clean dark-themed UI.

# 🔐 TMDB API
Add your API key inside app.py: TMDB_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# How to Run
pip install -r requirements.txt
python build_npz.py
streamlit run app.py

# Live Demo
🔗 https://cinexplain-movie-recommender.streamlit.app/