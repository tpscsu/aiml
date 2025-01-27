import random


def generate_quote():
    quotes = [
        "Your journey is as unique as your fingerprint.",
        "Focus on the step in front of you, not the whole staircase.",
        "Every accomplishment starts with the decision to try.",
        "When you feel like giving up, remember why you started.",
        "Even if the ground shakes , your hands shouldn't."
    ]

    random_quote = random.choice(quotes)
    print("\nQuote for you:")
    print(f"\"{random_quote}\"")


if __name__ == "__main__":
    print("Welcome to the Random Motivational Quote Generator!")
    generate_quote()
