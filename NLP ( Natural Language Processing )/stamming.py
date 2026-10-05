import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

text = "The Students are studying and playing games."

words = word_tokenize(text)
stemmer = PorterStemmer()

stemmer_words = [stemmer.stem(word) for word in words]
print("Original words : ")

print(words)

print("\n After Stemming : ")
print(stemmer_words)