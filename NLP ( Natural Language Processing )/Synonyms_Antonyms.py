import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

word = "active"

synonyms = set()
antonyms = set()

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())
        
        if lemma.antonyms():
            for ant in lemma.antonyms():
                antonyms.add(ant.name())

print("Word:", word)

print("\nSynonyms:")
print(synonyms)

print("\nAntonyms:")
print(antonyms)