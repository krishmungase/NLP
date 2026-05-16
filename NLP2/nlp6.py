# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load real dataset
df = pd.read_csv("review.csv")
print(f"Dataset shape: {df.shape}")
print(df["sentiment"].value_counts())

texts = df["review"].astype(str).tolist()
labels = df["sentiment"].tolist()

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42, stratify=labels
)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words="english", max_features=20000, ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
print(f"TF-IDF matrix shape: {X_train_vec.shape}")

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(classification_report(y_test, y_pred))

test = [
    "This movie is amazing, I loved every minute of it",
    "Worst film I have ever seen, complete waste of time",
    "The acting was great but the plot was a bit slow",
    
    "Absolutely fantastic storyline and brilliant performances",
    "I fell asleep halfway through, it was so boring",
    "The visuals were stunning, but the script needed work",
    "One of the best movies this year, highly recommended",
    "Terrible editing and weak character development",
    "It had some funny moments, but overall it was average",
    "A masterpiece with an emotional ending",
    "Not bad, but I expected much more from the director",
    "The soundtrack was incredible and fit perfectly",
    "Awful acting ruined what could have been a good film"
]

# Transform test text
test_vector = vectorizer.transform(test)

# Predict sentiment
predictions = model.predict(test_vector)

for sentence, pred in zip(test, predictions):
    print(f"[{pred}] {sentence}")