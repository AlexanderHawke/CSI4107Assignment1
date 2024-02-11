import os
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def preprocess(documents):
    with open('stopwords.txt', 'r') as file:
        stopwords = file.read().splitlines()

    punctuation = set(string.punctuation)
    punctuation.remove('-')
    print(punctuation)

    porterStemmer = PorterStemmer()

    for subDoc in documents:
        text = documents[subDoc].lower()
        tokens = word_tokenize(text)
        # Remove punctuation from tokens list
        tokens = [token for token in tokens if token not in punctuation and not any(char.isdigit() for char in token)]
        # Stem the words and remove stopwords
        tokens = [porterStemmer.stem(word) for word in tokens if word not in stopwords]
        documents[subDoc] = tokens
        print(documents[subDoc])

