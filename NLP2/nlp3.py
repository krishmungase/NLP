import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Elon Musk is the CEO of Tesla in California. He was born in South Africa. Tesla's stock price has been rising."
print("==== Input Text =====")
print(text)

doc = nlp(text)

# Print entities and labels
for ent in doc.ents:
    print(ent.text, " --> ", ent.label_)