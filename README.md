# Project on Recommendations on MovieLens Dataset & IMDB

Dataset : MovieLens(20M) https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset
Dataset : IMDB top 1000 https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-

Merged both to create our own Dataset for recommendations
- UserID
- MovieID
- Rating
- Title
- Timestamp
- Genre
- Overview

# Task
## Content based(Desc/Overview)
- TFIDF
- Transformer based(NLP,BERT)
   - Compare 3 algo with performance metrics 

## Collaborative 
- User User (Cosine Similarity)
- Item Item (Cosine Similarity)
- Two Tower Model
Output : Top K recommendations using performance metrics(Precision, recall)

## Session Based
- UserID, MovieID, Timestamp 
- Sort on timestamp, filter on UserID & make click data 
   
