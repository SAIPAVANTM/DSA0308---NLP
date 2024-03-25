import random

def build_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    model = {}
    for word1, word2 in bigrams:
        if word1 in model:
            model[word1].append(word2)
        else:
            model[word1] = [word2]
    return model

def generate_text_bigram(model, length=10):
    current_word = random.choice(list(model.keys()))
    text = [current_word]
    for _ in range(length-1):
        if current_word in model:  # Check if current_word is in the model
            next_word = random.choice(model[current_word])
            text.append(next_word)
            current_word = next_word
        else:
            break  # If current_word is not found in the model, break the loop
    return ' '.join(text)

# Example usage:
text = "The quick brown fox jumps over the lazy dog"
bigram_model = build_bigram_model(text)
generated_text = generate_text_bigram(bigram_model, length=20)
print(generated_text)
