# Install required libraries
%pip install gensim nltk scikit-learn matplotlib

# Import libraries
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

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

# ---------------------------------------------------
# 1. TOKENIZATION
# ---------------------------------------------------

# Tokenize sentences
data = [word_tokenize(review.lower()) for review in reviews]

print("==== Tokenized Reviews ====")

for i, review in enumerate(data):
    print(f"Review {i+1}: {review}")

# ---------------------------------------------------
# 2. TRAIN WORD2VEC MODEL
# ---------------------------------------------------

model = Word2Vec(
    sentences=data,
    vector_size=20,
    window=2,
    min_count=1,
    workers=1
)

# ---------------------------------------------------
# 3. SEMANTIC SIMILARITY
# ---------------------------------------------------

print("\n==== Words Similar to 'movie' ====")

similar_words = model.wv.most_similar("movie")

for word, score in similar_words:
    print(f"{word:15} --> {score:.4f}")

# ---------------------------------------------------
# 4. t-SNE VISUALIZATION
# ---------------------------------------------------

# Get word vectors
words = list(model.wv.index_to_key)
word_vectors = model.wv[words]

# Apply t-SNE
tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=3
)

word_vectors_2d = tsne.fit_transform(word_vectors)

# Plot words
plt.figure(figsize=(10, 7))

for i, word in enumerate(words):
    x, y = word_vectors_2d[i]
    plt.scatter(x, y)
    plt.text(x + 0.02, y + 0.02, word)

plt.title("t-SNE Visualization of Word Embeddings")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")

plt.show()