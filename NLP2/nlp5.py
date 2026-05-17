# Install required libraries
%pip install gensim nltk

# Import libraries
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

# Download tokenizer
nltk.download('punkt')

# Small movie review dataset
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
model = Word2Vec(
    sentences=data,
    vector_size=20,
    window=2,
    min_count=1,
    workers=1
)

# Find similar words
print("\n==== Words Similar to 'movie' ====")

similar_words = model.wv.most_similar("movie")

for word, score in similar_words:
    print(f"{word:15} --> {score:.4f}")