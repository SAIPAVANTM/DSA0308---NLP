import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import DefaultTagger

# Example text
text = "The quick brown fox jumps over the lazy dog."

# Define transformation rules
transformation_rules = [
    (r'\bquick\b', 'JJ'),       # If word is 'quick', tag it as adjective (JJ)
    (r'\bbrown\b', 'JJ'),       # If word is 'brown', tag it as adjective (JJ)
    (r'\bfox\b', 'NN'),         # If word is 'fox', tag it as noun (NN)
    (r'\bjumps\b', 'VBZ'),      # If word is 'jumps', tag it as verb (VBZ)
    (r'\bover\b', 'IN'),        # If word is 'over', tag it as preposition (IN)
    (r'\bthe\b', 'DT'),         # If word is 'the', tag it as determiner (DT)
    (r'\blazy\b', 'JJ'),        # If word is 'lazy', tag it as adjective (JJ)
    (r'\bdog\b', 'NN')          # If word is 'dog', tag it as noun (NN)
]

# Define a transformation-based tagger using the transformation rules
class TransformationTagger(nltk.TaggerI):
    def __init__(self, rules):
        self.rules = rules

    def tag(self, tokens):
        tagged_tokens = []
        for token in tokens:
            tagged_token = token
            for pattern, tag in self.rules:
                if nltk.re.search(pattern, token[0]):
                    tagged_token = (token[0], tag)
                    break
            tagged_tokens.append(tagged_token)
        return tagged_tokens

# Apply transformation-based tagging to the example text
tokens = nltk.pos_tag(word_tokenize(text))
tagger = TransformationTagger(transformation_rules)
transformed_tags = tagger.tag(tokens)

# Print the transformed tags
print(transformed_tags)
