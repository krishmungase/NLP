# Install scikit-learn
%pip install scikit-learn

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
labels = [
    "Positive",
    "Positive",
    "Negative",
    "Negative"
]

# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

print("==== TF-IDF Matrix Created Successfully ====")

# Train Naive Bayes model
model = MultinomialNB()

model.fit(X, labels)

print("==== Model Trained Successfully ====")

# Test sentence
test = ["This movie is amazing"]

# Transform test text
test_vector = vectorizer.transform(test)

# Predict sentiment
prediction = model.predict(test_vector)

print("\n==== Prediction ====")
print("Sentence:", test[0])
print("Sentiment:", prediction[0])