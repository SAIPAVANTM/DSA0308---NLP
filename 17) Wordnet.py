import nltk
from nltk.corpus import wordnet

# Download NLTK resources
nltk.download('wordnet')

def explore_word_meanings(word):
    # Retrieve synsets for the word
    synsets = wordnet.synsets(word)
    
    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - Definition: {synset.definition()}")
            print(f" - Examples: {synset.examples()}")
            print()
    else:
        print(f"No synsets found for '{word}'")

# Word to explore
word_to_explore = "car"

# Explore word meanings
explore_word_meanings(word_to_explore)
