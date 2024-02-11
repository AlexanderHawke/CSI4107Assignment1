import math
from collections import defaultdict
from math import log

def compute_idf(inverted_index, numDocs):
    idf_scores = {}
    for term, docs in inverted_index.items():
        # The number of documents containing the term is the length of the docs list
        doc_freq = len(docs)
        # Use the IDF formula as specified
        idf_scores[term] = log(numDocs / doc_freq, 10)
    
    return idf_scores

def compute_tf_idf(inverted_index, idf_scores, num_docs):
    tf_idf_scores = {}

    for term, doc_dict in inverted_index.items():
        for doc_id, term_freq in doc_dict.items():
            # The Term Frequency is the raw count of how many times a word occurs in a document in this case
            # Retrieve the corresponding IDF score for that term
            idf = idf_scores.get(term, log(num_docs, 10))  # Default IDF if term is not found
            # Calculate TF-IDF score
            tf_idf = term_freq * idf
            # Initialize a nested dictionary if necessary
            if doc_id not in tf_idf_scores:
                tf_idf_scores[doc_id] = {}
            # Assign the TF-IDF score to the term for this document
            tf_idf_scores[doc_id][term] = tf_idf

    return tf_idf_scores

import math

def compute_document_lengths(tfidfScores):
    doc_lengths = {}

    for doc_id, scores in tfidfScores.items():
        # Calculate the square root of the sum of the squares of TF-IDF scores for the document
        length = math.sqrt(sum(tfidf**2 for tfidf in scores.values()))
        doc_lengths[doc_id] = length

    return doc_lengths

# Function to convert the query into its vector representation using term frequency and inverse document frequency.
def build_query_vector(query_terms, idf_values, docs_count):
    term_freq = defaultdict(int)
    # Count the frequency of each term in the query
    for term in query_terms:
        term_freq[term] += 1
    
    # Calculate the query vector with IDF weighting
    query_vec = {}
    for term, freq in term_freq.items():
        # Use the IDF value if the term is in the idf_values, otherwise assume 0
        term_idf = idf_values.get(term, math.log(docs_count))  # Default IDF if term not found should not be 0
        query_vec[term] = freq * term_idf
    
    return query_vec

# Function to calculate the cosine similarity between two vectors.
def cosine_sim(vec_a, vec_b):
    # Calculate the dot product
    dot_prod = sum(vec_a.get(term, 0) * vec_b.get(term, 0) for term in set(vec_a.keys()).union(vec_b.keys()))
    # Calculate the magnitude of the vectors
    mag_a = math.sqrt(sum(value ** 2 for value in vec_a.values()))
    mag_b = math.sqrt(sum(value ** 2 for value in vec_b.values()))
    # Avoid division by zero
    if mag_a == 0 or mag_b == 0:
        return 0
    # Calculate cosine similarity
    cosine_sim_val = dot_prod / (mag_a * mag_b)
    
    return cosine_sim_val

# Function to retrieve and rank documents based on cosine similarity.
def retrieve_and_rank(query, index, idf, lengths_of_docs, total_num_docs):
    # Build the query vector
    query_vec = build_query_vector(query.lower().split(), idf, total_num_docs)
    
    # Initialize dictionary to store similarity scores
    doc_scores = defaultdict(float)
    
    # Calculate scores for each document containing terms from the query
    for term in query_vec:
        if term in index:
            for doc_id, term_freq in index[term].items():
                doc_vec = {term: term_freq * idf.get(term, 0)}
                # Calculate cosine similarity for each document
                sim_score = cosine_sim(doc_vec, query_vec)
                # Add to total score for the document
                doc_scores[doc_id] += sim_score
    
    # Normalize the scores
    for doc_id, score in doc_scores.items():
        length = lengths_of_docs.get(doc_id, 1)
        doc_scores[doc_id] = score / length  # Avoid division by zero by defaulting length to 1
    
    return doc_scores

# Call the function to retrieve and rank documents
# document_scores = retrieve_and_rank(query, inverted_index, idf_scores, doc_lengths, total_docs)

# Sort the documents based on their scores in descending order
# sorted_documents = sorted(document_scores.items(), key=lambda item: item[1], reverse=True)