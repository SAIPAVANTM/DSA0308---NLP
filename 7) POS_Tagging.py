import nltk
from nltk.tokenize import word_tokenize

# Download required resources
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_words = nltk.pos_tag(words)
    
    return tagged_words

# Example text

text = "The quick brown fox jumps over the lazy dog"

# Perform part-of-speech tagging
tagged_text = pos_tagging(text)

# Print the tagged text
print(tagged_text)

