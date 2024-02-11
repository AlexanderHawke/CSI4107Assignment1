import os
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
import re  # Import regular expressions

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def preprocess(documents):
    with open('stopwords.txt', 'r') as file:
        stopwords = file.read().splitlines()

    punctuation = set(string.punctuation)
    punctuation.remove('-')  # Keep hyphenated words

    lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(treebank_tag):
        # Converts treebank tags to wordnet tags.
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to noun if unknown

    def is_numeric(token):
        # Returns True if the token is numeric (including numbers with punctuation)
        return bool(re.search(r'\d', token))

    for doc_id, text in documents.items():
        tokens = word_tokenize(text.lower())  # Tokenize text
        # Update the condition to use is_numeric for filtering
        tokens = [token for token in tokens if not is_numeric(token) and token not in punctuation and token not in {"'s", "``", "''"}]
        tagged_tokens = pos_tag(tokens)  # Part-of-speech tagging
        
        # Lemmatize words with appropriate POS tag
        lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged_tokens]
        
        # Remove stopwords after lemmatization
        final_tokens = [token for token in lemmatized_tokens if token not in stopwords]
        
        documents[doc_id] = final_tokens
