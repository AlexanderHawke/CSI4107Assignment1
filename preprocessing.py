import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def preprocess(documents):
    with open('stopwords.txt', 'r') as file:
        stopwords = file.read().splitlines()

    for subDoc in documents: 
        # Text: documents[subDoc]
        documents[subDoc] = word_tokenize(documents[subDoc]) # this doesnt work for some reason

