class PluralFiniteStateMachine:
    def generate_plural(self, noun):
        if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return noun + 'es'
        elif noun.endswith('y') and noun[-2] not in 'aeiou':
            return noun[:-1] + 'ies'
        else:
            return noun + 's'


def main():
    fsm = PluralFiniteStateMachine()

    nouns = ['cat', 'dog', 'church', 'boy', 'box', 'fox', 'buzz', 'party', 'city']

    for noun in nouns:
        plural = fsm.generate_plural(noun)
        print(f"The plural of '{noun}' is '{plural}'.")


if __name__ == "__main__":
    main()
