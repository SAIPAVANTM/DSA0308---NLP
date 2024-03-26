class CFG:
    def __init__(self, start_symbol, productions):
        self.start_symbol = start_symbol
        self.productions = productions

    def generate(self):
        return self.expand(self.start_symbol)

    def expand(self, symbol):
        import random
        if symbol not in self.productions:
            return symbol
        else:
            production = random.choice(self.productions[symbol])
            return ''.join(self.expand(s) for s in production)


# Example usage:
grammar = CFG('S', {
    'S': ['aS', 'bS', '']
})

generator = grammar.generate
for _ in range(5):
    print(generator())
