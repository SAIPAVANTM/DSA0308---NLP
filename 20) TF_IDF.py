from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "TF-IDF stands for term frequency-inverse document frequency.",
    "It is a numerical statistic used to reflect the importance of a word in a document.",
    "TF-IDF value increases proportionally to the number of times a word appears in the document.",
    "But is often offset by the frequency of the word in the corpus.",
    "Cosine similarity is a measure of similarity between two non-zero vectors in an inner product space."
]

# Query
query = "TF-IDF is used for document ranking."

# Compute TF-IDF matrix for documents
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Compute TF-IDF vector for the query
query_vector = tfidf_vectorizer.transform([query])

# Calculate cosine similarity between query vector and document vectors
cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

# Rank documents based on cosine similarity
ranked_documents_indices = cosine_similarities.argsort()[::-1]
ranked_documents = [(cosine_similarities[i], documents[i]) for i in ranked_documents_indices]

# Print ranked documents
print("Ranked Documents:")
for rank, (score, document) in enumerate(ranked_documents, start=1):
    print(f"Rank {rank}: Score = {score}, Document = '{document}'")
