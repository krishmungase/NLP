# Install spaCy
%pip install spacy

# Download English model
!python -m spacy download en_core_web_sm

# Import spaCy
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Elon Musk is the CEO of Tesla in California. He was born in South Africa. Tesla's stock price has been rising."

print("==== Input Text =====")
print(text)

# Process text
doc = nlp(text)

# Print Named Entities
print("\n==== Named Entities =====")

for ent in doc.ents:
    print(ent.text, " --> ", ent.label_)