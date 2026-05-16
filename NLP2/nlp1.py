import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizeri

# Downloads
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "Natural Language Processing is amazing. NLP helps computers understand human language. It is very useful."


# Tokenization
tokens = word_tokenize(text)
print("=== 1. Sentence Tokenization ===")
for s in tokens: print("  •", s)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]
print("=== 2. After Stopword Removal ===")
for s in filtered: print("  •", s)

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in filtered]
print("\n=== 4. Stemming (PorterStemmer) ===")
for w in stemmed:
    print(f"  {w:15} ──► {ps.stem(w)}")


# Lemmatization
lm = WordNetLemmatizer()
lemmatized = [lm.lemmatize(word) for word in filtered]

print("\n=== 5. Lemmatization (dictionary) ===")
for w, l in zip(filtered, lemmatized):
    print(f"  {w:15} ──► {l}")