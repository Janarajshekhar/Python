import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
text = "Natural Language Processing is a branch of Artificial Intelligence."
tokens = word_tokenize(text)
print("Original text : ")
print(text)
print("\n Tokens : ")
print(tokens)

stop_words = set(stopwords.words('english'))
filtered_tokens = []
for word in tokens:
    if word.lower() not in stop_words:
        filtered_tokens.append(word)
print("\n Tokens after stop word removal : ")
print(filtered_tokens)