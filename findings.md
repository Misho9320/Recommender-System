# Movie Recommendation System - Findings

## Reflection on Movie Recommendation Methods

In this experiment, both **Collaborative Filtering (CF)** and **Content-Based Filtering (CBF)** were used to recommend movies to users. Overall, **Collaborative Filtering performed better** in this dataset. CF was able to recommend at least one movie to every user, including User 9, whereas CBF sometimes failed to generate recommendations, as seen for User 9.  

The reason CBF did not recommend any movies for User 9 is that it relies on the genres of movies that the user has already rated highly. If a user has rated very few movies or none with high ratings, there is insufficient data to find similar movies based on genre, resulting in an empty recommendation list.

## Challenges Faced

- Handling missing data in the user-item matrix, as not all users rated all movies.  
- Accommodating Content-Based Filtering required **adding movies to the dataset** and including a **new column called `genre`** to compute similarities between movies.  
- Cold-start problem: CF struggles with new users or items that have few ratings, whereas CBF can somewhat mitigate this if metadata like genres is available.

## Summary

While CBF provides richer recommendations based on movie attributes, CF proved more reliable in this dataset because it could still recommend items even for users with few ratings.
