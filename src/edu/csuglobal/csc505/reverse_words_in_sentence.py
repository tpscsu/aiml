def reverse_words_in_sentence():
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("Input cannot be empty.")
        return

    words = sentence.split()
    reversed_words = " ".join(reversed(words))

    print(f"Original Sentence: {sentence}")
    print(f"Reversed Word Order: {reversed_words}")


if __name__ == "__main__":
    reverse_words_in_sentence()
