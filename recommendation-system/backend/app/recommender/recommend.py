import numpy as np


def recommend_movies(user_id, user_item, similarity, top_n=5):

    idx = user_item.index.tolist().index(user_id)

    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

    similar_users = [i[0] for i in sim_scores[:5]]

    recommendations = (
        user_item.iloc[similar_users]
        .mean()
        .sort_values(ascending=False)
    )

    return recommendations.head(top_n).index.tolist()
