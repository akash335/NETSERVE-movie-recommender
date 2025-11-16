
# CineXplain — YouTube-style Netflix Movie Recommender

This UI is designed to look like the YouTube tutorial screenshot:

- Top horizontal **poster carousel**.
- Centered dark box with **dropdown search**.
- Big red **"Show Recommendation"** button.
- Grid of posters for recommended movies (5 per row).

## Usage

1. Copy your `movie_data.pkl` next to `app.py`.
   - The pickle must contain:
     - a DataFrame of movies (with columns `title` and `movie_id` or `id`/`movieId`),
     - a cosine similarity matrix (NumPy array or SciPy sparse) aligned with that DataFrame.
2. Add your TMDB key:
   - EITHER create `.env` with

         TMDB_API_KEY=YOUR_TMDB_V3_KEY

   - OR open `app.py` and replace `PASTE_YOUR_KEY_HERE` with your key.
3. Install requirements and run:

       pip install -r requirements.txt
       streamlit run app.py
