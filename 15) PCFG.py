import random

class PCFGParser:
    def __init__(self, pcfg):
        self.pcfg = pcfg

    def generate_sentence(self):
        return self.expand_symbol(self.pcfg['S'])

    def expand_symbol(self, symbol):
        if isinstance(symbol, str):  # Terminal symbol
            return symbol
        else:  # Non-terminal symbol
            productions = symbol
            probabilities = [prod[1] for prod in productions]
            chosen_production = random.choices(productions, probabilities)[0]
            return ''.join(self.expand_symbol(s) for s in chosen_production[0])


# Example usage:
pcfg = {
    'S': [
        (['NP', 'VP'], 0.7),
        (['Aux', 'VP'], 0.3)
    ],
    'NP': [
        ('I', 0.5),
        ('he', 0.3),
        ('she', 0.2)
    ],
    'VP': [
        (['V', 'NP'], 0.6),
        ('eats', 0.4)
    ],
    'V': [
        ('eats', 0.8),
        ('reads', 0.2)
    ],
    'Aux': [
        ('does', 1.0)
    ]
}

parser = PCFGParser(pcfg)

# Generate a sentence
sentence = parser.generate_sentence()
print("Generated Sentence:", sentence)
