import pandas as pd

def load_ratings():
    return pd.read_csv(
        r"C:\Users\Malini Elumalai\Downloads\ml-latest-small\ml-latest-small\ratings.csv"
    )
def load_movies():
    return pd.read_csv("C:/Users/Malini Elumalai/Downloads/ml-latest-small/ml-latest-small/movies.csv")