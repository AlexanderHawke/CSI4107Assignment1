import os
import preprocessing
import indexing
import retrievalandranking
import nltk

queries = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        queries.append