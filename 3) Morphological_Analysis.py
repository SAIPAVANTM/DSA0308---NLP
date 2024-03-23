import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')

# Sample text
text = "He eats apples and oranges. She is eating an apple now."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Perform morphological analysis
lemmatized_tokens = []
for token in tokens:
    lemmatized_token = lemmatizer.lemmatize(token)
    lemmatized_tokens.append(lemmatized_token)

# Print original tokens and their lemmatized forms
for original, lemmatized in zip(tokens, lemmatized_tokens):
    print(f"Original: {original} \t Lemmatized: {lemmatized}")
