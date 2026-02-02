import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def train_model(ratings):
    user_item = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating"
    ).fillna(0)

    similarity = cosine_similarity(user_item)

    return user_item, similarity
