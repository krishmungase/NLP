# NLP 6 with confusion matrix and classification report
# Install libraries
%pip install scikit-learn matplotlib seaborn

# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import seaborn as sns

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

# TF-IDF conversion
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Testing data
test = [
    "This movie is amazing",
    "I hate this film"
]

actual = [
    "Positive",
    "Negative"
]

# Convert test data
test_vector = vectorizer.transform(test)

# Predict
prediction = model.predict(test_vector)

# Accuracy
accuracy = accuracy_score(actual, prediction)

print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(actual, prediction,
                      labels=["Positive", "Negative"])

print("\nConfusion Matrix:\n")
print(cm)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(actual, prediction))

# Visualize confusion matrix
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=["Positive", "Negative"],
            yticklabels=["Positive", "Negative"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()