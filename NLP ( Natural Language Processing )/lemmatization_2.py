import spacy
nlp = spacy.load("en_core_web_sm")

text = "The cats were running much faster then the dogs."

doc = nlp(text)

lemmatized_word = [token.lemma_ for token in doc]
print("ORIGINAL TEXT : ",text)
print("Lemmatized : "," ".join(lemmatized_word))