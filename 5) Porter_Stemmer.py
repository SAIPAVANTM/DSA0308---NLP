import nltk
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
porter = PorterStemmer()

# List of words to be stemmed
words = ['running', 'runs', 'runner', 'ran', 'easily', 'fairly', 'fairness']

# Perform stemming on each word
stemmed_words = [porter.stem(word) for word in words]

# Print original words and their stemmed forms
for original, stemmed in zip(words, stemmed_words):
    print(f"Original: {original} \t Stemmed: {stemmed}")
