import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def perform_ner(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Named Entity Recognition
    named_entities = ne_chunk(tagged_words)
    
    # Iterate over each entity and print its text and label
    for entity in named_entities:
        if hasattr(entity, 'label'):
            print(f"Entity: {' '.join(child[0] for child in entity.leaves())}, Label: {entity.label()}")

# Example text
text = "Apple is a company based in Cupertino, California. Steve Jobs co-founded it."

# Perform Named Entity Recognition (NER) on the text
perform_ner(text)
