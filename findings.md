Reflection on Movie Recommendation Methods

In this experiment, both Collaborative Filtering (CF) and Content-Based Filtering (CBF) were used to recommend movies to users. Overall, Collaborative Filtering performed better in this dataset. CF was able to recommend at least one movie to every user, including User 9, whereas CBF sometimes failed to generate recommendations, as seen for User 9. The reason CBF did not recommend any movies for User 9 is that it relies on the genres of movies that the user has already rated highly. If a user has rated very few movies or none with high ratings, there is insufficient data to find similar movies based on genre, resulting in an empty recommendation list.

Challenges faced during the experiment included handling missing data in the user-item matrix, since not all users had rated all movies. To accommodate Content-Based Filtering, we had to add movies to the dataset and include a new column called 'genre', ensuring that the system could compute similarities between movies. Additionally, CF struggles with the cold-start problem, where new users or items with few ratings make it difficult to generate accurate recommendations, whereas CBF can somewhat mitigate this if movie metadata (like genres) is available.

In summary, while CBF provides richer recommendations based on movie attributes, CF proved more reliable in this dataset because it could still recommend items even for users with few ratings.

