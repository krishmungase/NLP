# Install NLTK
%pip install nltk

# Import libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import Counter

# Download required datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "Natural Language Processing is amazing. NLP helps computers understand human language. It is very useful."

# Tokenization
tokens = word_tokenize(text)

print("=== 1. Word Tokenization ===")
for word in tokens:
    print("•", word)

# Stopword Removal
stop_words = set(stopwords.words('english'))

filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("\n=== 2. After Stopword Removal ===")
for word in filtered_words:
    print("•", word)

# Stemming
ps = PorterStemmer()

stemmed_words = [ps.stem(word) for word in filtered_words]

print("\n=== 3. Stemming ===")
for word in stemmed_words:
    print("•", word)

# Lemmatization
lm = WordNetLemmatizer()

lemmatized_words = [lm.lemmatize(word) for word in filtered_words]

print("\n=== 4. Lemmatization ===")
for word in lemmatized_words:
    print("•", word)

# Morphology Analysis
print("\n=== 5. Morphology Analysis ===")
for word in filtered_words:
    print(f"Original Word: {word}")
    print(f"Stemmed Word : {ps.stem(word)}")
    print(f"Lemma Word   : {lm.lemmatize(word)}")
    print("---------------------------")

# Frequency Analysis
print("\n=== 6. Frequency Analysis ===")

# Convert words to lowercase and remove punctuation
clean_words = [word.lower() for word in filtered_words if word.isalpha()]

freq = Counter(clean_words)

for word, count in freq.items():
    print(f"{word} : {count}")