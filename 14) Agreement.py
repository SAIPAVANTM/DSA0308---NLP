class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar

    def check_agreement(self, sentence):
        words = sentence.split()
        parse_tree = self.parse_sentence(words)
        if parse_tree:
            return self.traverse_tree(parse_tree)
        else:
            return False

    def parse_sentence(self, words):
        # Implementation of parsing sentences based on the given grammar
        # You can use Earley parser or any other parsing algorithm here
        # For simplicity, we'll assume the sentence structure is already parsed
        # and represented as a tree
        return ParseTreeNode('S', [ParseTreeNode(word) for word in words])

    def traverse_tree(self, node):
        # Traverses the parse tree and checks for agreement
        if node.value == 'S':
            for child in node.children:
                if self.traverse_tree(child):
                    return True
            return False
        elif node.value == 'NP':
            noun_count = 0
            for child in node.children:
                if self.traverse_tree(child):
                    noun_count += 1
            return noun_count == 1
        elif node.value == 'VP':
            verb_count = 0
            for child in node.children:
                if self.traverse_tree(child):
                    verb_count += 1
            return verb_count == 1
        elif node.value == 'N':
            return True  # Assume all nouns agree
        elif node.value == 'V':
            return True  # Assume all verbs agree
        else:
            return False  # Non-terminal nodes, ignore


class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)


# Example usage:
# Define a simple context-free grammar
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['N'], ['Adj', 'N']],
    'VP': [['V'], ['V', 'NP']],
    'N': ['dog', 'cat', 'house'],
    'Adj': ['big', 'small'],
    'V': ['chases', 'sleeps']
}

# Initialize the agreement checker with the grammar
checker = AgreementChecker(grammar)

# Test sentences
sentences = [
    "dog chases cat",
    "dog chases cats",
    "dogs chases cat",
    "dogs chase cats",
    "big cat chases dog"
]

# Check agreement in each sentence
for sentence in sentences:
    agreement = checker.check_agreement(sentence)
    print(f"Sentence: '{sentence}' => Agreement: {agreement}")
