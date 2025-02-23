from num2words import num2words


def convert_to_words(amount):
    """
    Converts a numeric dollar amount into words formatted for a check.
    """
    try:
        # Convert input to float and format it with two decimal places
        dollars, cents = map(int, f"{float(amount):.2f}".split("."))

        # Convert the dollar part to words
        dollar_words = num2words(dollars, lang='en').capitalize()

        # Convert cents separately
        if cents == 0:
            cents_words = "zero cents"
        else:
            cents_words = num2words(cents, lang='en') + " cents"

        return f"{dollar_words} dollars and {cents_words}"

    except ValueError:
        return "Invalid input. Please enter a valid numeric amount."


amount = input("Enter the amount in dollars: ")
print("Check Amount in Words:", convert_to_words(amount))
