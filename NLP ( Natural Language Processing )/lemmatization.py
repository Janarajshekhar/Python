import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
text = "The students are studying and playing games."

words = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
lemmatized_word = [lemmatizer.lemmatize(word) for word in words]

print("Original words : ")
print(words)
print("\n After lemmatization : ")
print(lemmatized_word)