class FiniteStateAutomaton:
    def __init__(self):
        self.state = 'q0'

    def transition(self, input_symbol):
        if self.state == 'q0' and input_symbol == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and input_symbol == 'b':
            self.state = 'q2'
        elif self.state == 'q2' and input_symbol == 'a':
            self.state = 'q1'
        else:
            self.state = None

    def reset(self):
        self.state = 'q0'

    def is_accepting(self):
        return self.state == 'q2'


def main():
    automaton = FiniteStateAutomaton()
    strings = ['ab', 'aab', 'abab', 'aabb', 'b', 'ba', 'aba']

    for string in strings:
        automaton.reset()
        for symbol in string:
            automaton.transition(symbol)
        if automaton.is_accepting():
            print(f"'{string}' is accepted")
        else:
            print(f"'{string}' is rejected")


if __name__ == "__main__":
    main()
