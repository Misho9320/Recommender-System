##Movie Recommendation System
#Overview

This project implements a simple Movie Recommendation System using two approaches:

Collaborative Filtering (CF) – Recommends movies based on similarities between users' ratings.

Content-Based Filtering (CBF) – Recommends movies based on similarity of movie genres.

The dataset contains user ratings for movies, and movie metadata including genres.

Dataset

File: movies.csv

Columns:

user_id – ID of the user

movie_title – Name of the movie

rating – User rating for the movie (numeric)

genre – Genres of the movie, separated by |

Note: The genre column was added to accommodate content-based filtering. Some movies were also added to the dataset to ensure a variety of recommendations.

Requirements

Python 3.x

pandas

numpy

scikit-learn

Install dependencies using:

pip install pandas numpy scikit-learn

How to Run

Place the dataset movies.csv in the same directory as the script.

Run the script:

python script.py


Enter a user_id when prompted to get movie recommendations.

Functionality

Collaborative Filtering (CF)

Creates a user-item rating matrix.

Computes similarity between users using cosine similarity.

Recommends movies that similar users rated highly.

Content-Based Filtering (CBF)

Converts movie genres into a feature matrix.

Computes similarity between movies based on genres.

Recommends movies similar to those the user rated highly (rating ≥ 4).

Note: CBF may not recommend movies if the user has not rated any movies highly, as seen with some users in testing.

Observations

CF tends to provide recommendations even for users with few ratings.

CBF is dependent on user-rated movies and metadata; without sufficient data, it may fail to recommend.

Adding the genre column was necessary to make CBF work properly.

Limitations & Challenges

Cold-start problem for new users or movies with no ratings.

Sparse user-item matrix can limit CF performance.

CBF recommendations depend heavily on movie metadata quality.

Results

The following screenshots show sample recommendations for different users:

User 5


User 19


User 9


Conclusion

The system demonstrates two complementary recommendation approaches. CF is more reliable for users with sufficient ratings, while CBF allows recommendations based on movie features, which is useful for new items or when ratings are sparse.

If you want, I can also write a short caption under each screenshot summarizing the recommendations, so

