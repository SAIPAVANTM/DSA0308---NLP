import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict


# Sample training corpus
training_corpus = [
    ("The", "DT"), ("quick", "JJ"), ("brown", "JJ"), ("fox", "NN"),
    ("jumps", "VBZ"), ("over", "IN"), ("the", "DT"), ("lazy", "JJ"), ("dog", "NN")
]

# Build probabilistic model
model = defaultdict(lambda: defaultdict(int))
for word, pos_tag in training_corpus:
    word = word.lower()
    pos_tag = pos_tag.upper()
    if word in model:
        model[word][pos_tag] += 1
    else:
        model[word][pos_tag] = 1

# Perform stochastic part-of-speech tagging
text = "The quick brown fox jumps over the lazy dog"
tagged_text = []
for word in word_tokenize(text):
    word = word.lower()
    if word in model:
        max_count = 0
        most_likely_tag = None
        for tag, count in model[word].items():
            if count > max_count:
                max_count = count
                most_likely_tag = tag
        tagged_text.append((word, most_likely_tag))
    else:
        tagged_text.append((word, 'NN'))  # Assign default tag 'NN' if word not found in model

# Print the tagged text
print(tagged_text)
