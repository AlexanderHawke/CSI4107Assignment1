from collections import defaultdict
import math

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