def execution_steps():
    steps = [
        "1. Define a class to store developer traits.",
        "2. Initialize a list of key traits.",
        "3. Implement a method to display the traits.",
        "4. Implement another method to print execution steps.",
        "5. Instantiate the class and call its methods."
    ]
    print("\nSteps in writing this program:")
    for step in steps:
        print(step)


class SoftwareDeveloperTraits:
    def __init__(self):
        self.traits = ["Analytical Thinking", "Problem-Solving", "Collaboration"]

    def describe_traits(self):
        print("Common personality traits among successful software developers:")
        for trait in self.traits:
            print(f"- {trait}")


# Program Execution
if __name__ == "__main__":
    dev_traits = SoftwareDeveloperTraits()
    dev_traits.describe_traits()
    execution_steps()
