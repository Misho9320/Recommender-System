# Movie Recommendation System

## Overview

This project implements a simple **Movie Recommendation System** using two approaches:

1. **Collaborative Filtering (CF)** – Recommends movies based on similarities between users' ratings.
2. **Content-Based Filtering (CBF)** – Recommends movies based on similarity of movie genres.

The dataset contains user ratings for movies, and movie metadata including genres.

---

## Dataset

* **File**: `movies.csv`
* **Columns**:

  * `user_id` – ID of the user
  * `movie_title` – Name of the movie
  * `rating` – User rating for the movie (numeric)
  * `genre` – Genres of the movie, separated by `|`

**Note:** The `genre` column was added to accommodate content-based filtering. Some movies were also added to the dataset to ensure a variety of recommendations.

---

## Requirements

* Python 3.x
* pandas
* numpy
* scikit-learn

Install dependencies using:

```bash
pip install pandas numpy scikit-learn
```

---

## How to Run

1. Place the dataset `movies.csv` in the same directory as the script.
2. Run the script:

```bash
python main.py
```

3. Enter a `user_id` when prompted to get movie recommendations.

---

## Functionality

1. **Collaborative Filtering (CF)**

   * Creates a user-item rating matrix.
   * Computes similarity between users using **cosine similarity**.
   * Recommends movies that similar users rated highly.

2. **Content-Based Filtering (CBF)**

   * Converts movie genres into a feature matrix.
   * Computes similarity between movies based on genres.
   * Recommends movies similar to those the user rated highly (rating ≥ 4).

**Note:** CBF may not recommend movies if the user has not rated any movies highly, as seen with some users in te
