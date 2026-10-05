import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The students are knowing Natural Language Processing"

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Original Text:")
print(text)

print("\nPOS Tagging:")

for word, tag in pos_tags:
    print(word, "->", tag)