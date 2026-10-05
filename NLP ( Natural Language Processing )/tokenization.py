import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
text = "Natural Language Processing is a branch of Artificial Intelligence."
tokens = word_tokenize(text)
print("\nOriginal text : ",text)
print("Tokens : ",tokens)