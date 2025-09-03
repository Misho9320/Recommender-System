import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore")


# Load dataset
df = pd.read_csv("movies.csv", delimiter=";")
df.columns = df.columns.str.strip()
print(df.head())

# -------------------------------
# Ask which user to recommend for
# -------------------------------
try:
    target_user = int(input("\nEnter a user_id to recommend for: "))
except ValueError:
    print("Invalid input. Please enter a numeric user_id.")
    exit()

if target_user not in df["user_id"].unique():
    print(f"user_id {target_user} not found in dataset.")
    exit()

# 1. Collaborative Filtering
user_item_matrix = df.pivot_table(index="user_id", columns="movie_title", values="rating")
print(user_item_matrix)

# Fill NaN with 0 for similarity calculation
matrix_filled = user_item_matrix.fillna(0)

# Compute similarity between users
user_similarity = cosine_similarity(matrix_filled)
print("User Similarity Matrix:\n", user_similarity)

# Map user_id to its row index in the matrix
user_index = list(user_item_matrix.index).index(target_user)

similar_users = user_similarity[user_index]
most_similar_user = np.argsort(similar_users)[-2]  # most similar (excluding self)

# Get movies rated by most similar user
recommended_movies_cf = user_item_matrix.iloc[most_similar_user].dropna().index.tolist()
print(f"\nCollaborative Filtering → Recommended movies for User {target_user}: {recommended_movies_cf}")

# 2. Content-Based Filtering
# We added a genre column to the dataset
if "genre" in df.columns:
    # Convert movie genres into a feature matrix
    count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
    genre_matrix = count_vectorizer.fit_transform(df["genre"].fillna(""))

    # Compute cosine similarity between movies
    movie_similarity = cosine_similarity(genre_matrix)

    # Get movies the target user has rated
    user_movies = df[df["user_id"] == target_user]

    # Pick movies that target user rated highly
    high_rated_movies = user_movies[user_movies["rating"] >= 4]["movie_title"].tolist()

    recommended_movies_cb = []
    for movie in high_rated_movies:
        idx = df[df["movie_title"] == movie].index[0]
        similar_scores = list(enumerate(movie_similarity[idx]))
        similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
        top_movies = [df.iloc[i[0]]["movie_title"] for i in similar_scores[1:6]]
        recommended_movies_cb.extend(top_movies)

    print(f"\nContent-Based Filtering → Recommended movies for User {target_user}: {list(set(recommended_movies_cb))}")
else:
    print("\nContent-Based Filtering skipped (no 'genres' column in dataset).")
