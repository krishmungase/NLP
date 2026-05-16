from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Small real-style movie review dataset
reviews = [
    "The movie was fantastic and inspiring",
    "I really loved the acting and story",
    "The film was boring and slow",
    "Amazing direction and wonderful screenplay",
    "The movie was terrible and disappointing"
]

# Tokenize sentences
data = [word_tokenize(review.lower()) for review in reviews]
print("==== Tokenized Reviews ====")
for i, review in enumerate(data):
    print(f"Review {i+1}: {review}")

    # Train Word2Vec model
model = Word2Vec(data,
                 vector_size=20,
                 window=2,
                 min_count=1,
                 workers=1)

# Find similar words
print("Words similar to 'movie':\n")
print(model.wv.most_similar("movie"))