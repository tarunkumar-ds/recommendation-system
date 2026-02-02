from fastapi import FastAPI
from app.recommender.data_loader import load_ratings, load_movies
from app.recommender.model import train_model
from app.recommender.recommend import recommend_movies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Mini Recommendation System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ratings = load_ratings()
movies = load_movies()
user_item, similarity = train_model(ratings)
movie_map = dict(zip(movies.movieId, movies.title))


@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    if user_id not in user_item.index:
        return {"error": "User ID not found"}

    movie_ids = recommend_movies(user_id, user_item, similarity)
    movie_titles = [movie_map.get(mid, "Unknown") for mid in movie_ids]

    return {
        "user_id": user_id,
        "recommended_movies": movie_titles
    }

