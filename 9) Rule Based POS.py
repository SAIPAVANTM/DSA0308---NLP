import re
from nltk.tokenize import word_tokenize

# Define the rules for part-of-speech tagging using regular expressions
rules = [
    (r'\b(?:is|am|are|was|were)\b', 'VB'),  # Verbs
    (r'\b(?:a|an|the)\b', 'DT'),             # Determiners
    (r'\b(?:quick|brown|lazy)\b', 'JJ'),     # Adjectives
    (r'\b(?:fox|dog)\b', 'NN'),              # Nouns
    (r'\b(?:over)\b', 'IN'),                 # Prepositions
    (r'\b(?:jumps)\b', 'VBZ'),               # Verbs
    (r'\b(?:\.)\b', '.'),                    # Punctuation
    (r'\b(?:\w+)\b', 'NN')                   # Default: Nouns
]

# Function to perform rule-based part-of-speech tagging
def rule_based_pos_tagging(text, rules):
    tagged_text = []
    for word in word_tokenize(text):
        for pattern, tag in rules:
            if re.match(pattern, word):
                tagged_text.append((word, tag))
                break
        else:
            tagged_text.append((word, 'NN'))  # Default to noun if no rule matches
    return tagged_text

# Example text
text = "The quick brown fox jumps over the lazy dog."

# Perform rule-based part-of-speech tagging
tagged_text = rule_based_pos_tagging(text, rules)

# Print the tagged text
print(tagged_text)
