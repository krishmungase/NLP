# Import spaCy
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking at buying U.K. startup for $1 billion. The deal is expected to close by the end of the year."
print("=== Original Text ===")
print(text)

# Process text with spaCy
doc = nlp(text)

# Print tokens and their POS tags
print("\n=== Tokens and POS Tags ===")
for token in doc:
    print(f"  {token.text:15} ──► {token.pos_}")