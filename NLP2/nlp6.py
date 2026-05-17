# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset
texts = [
    "I love this movie",
    "This film was amazing",
    "I hate this movie",
    "The movie was boring"
]

# Labels
labels = ["Positive", "Positive", "Negative", "Negative"]

# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
test = ["This movie is amazing"]

# Transform test text
test_vector = vectorizer.transform(test)

# Predict sentiment
prediction = model.predict(test_vector)

print("Prediction:", prediction[0])