# Install NLTK
%pip install nltk

# Import library
from nltk.util import ngrams

# Sample text
text = "I am learning natural language processing. It is very interesting. I enjoy working with text data."

print("==== Original Text ====")
print(text)

# Split text into words
words = text.split()

print("\n==== Words ====")
print(words)

# Generate Bigrams
bigrams = list(ngrams(words, 2))

# Generate Trigrams
trigrams = list(ngrams(words, 3))

print("\n==== Bigrams ====")
for bg in bigrams:
    print(bg)

print("\n==== Trigrams ====")
for tg in trigrams:
    print(tg)