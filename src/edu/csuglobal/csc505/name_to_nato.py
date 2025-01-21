def name_to_nato():
    nato_alphabet = {
        "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
        "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
        "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
        "Z": "Zulu"
    }

    name = input("Enter a name: ").strip().upper()

    if not name.isalpha():
        print("Invalid input. Please enter only alphabetic characters.")
        return

    phonetic_representation = [nato_alphabet[char] for char in name]
    print("NATO Phonetic Alphabet Representation:")
    print(" ".join(phonetic_representation))


if __name__ == "__main__":
    name_to_nato()
