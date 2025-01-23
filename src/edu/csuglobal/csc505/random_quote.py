import random


def generate_quote():
    quotes = [
        "The smallest step in the right direction can end up being the biggest step of your life.",
        "Challenges are what make life interesting; overcoming them is what makes life meaningful.",
        "Your growth begins where your comfort zone ends.",
        "Focus on the step in front of you, not the whole staircase.",
        "Don’t count the days; make the days count.",
        "Success is the sum of small efforts repeated day in and day out.",
        "A goal without a plan is just a wish.",
        "Every accomplishment starts with the decision to try.",
        "When you feel like giving up, remember why you started.",
        "What you do today can improve all your tomorrows."
    ]

    random_quote = random.choice(quotes)
    print("\nHere’s your motivational quote:")
    print(f"\"{random_quote}\"")


if __name__ == "__main__":
    print("Welcome to the Random Motivational Quote Generator!")
    generate_quote()
