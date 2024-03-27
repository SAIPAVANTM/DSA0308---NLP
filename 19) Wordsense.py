import nltk
nltk.download('stopwords')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk(word, sentence):
    best_sense = None
    max_overlap = 0
    word = word.lower()
    context = set(word_tokenize(sentence))
    context = context.difference(stopwords.words('english'))
    for sense in wordnet.synsets(word):
        signature = set(word_tokenize(sense.definition()))
        for example in sense.examples():
            signature.union(set(word_tokenize(example)))
        signature = signature.difference(stopwords.words('english'))
        overlap = len(signature.intersection(context))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return best_sense

# Example usage
word = "bank"
sentence = "I went to the bank to deposit my money."
sense = lesk(word, sentence)
print("Word:", word)
print("Sense:", sense)
print("Definition:", sense.definition())
