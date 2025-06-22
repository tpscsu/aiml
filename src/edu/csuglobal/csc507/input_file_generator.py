import random
import os

FILES_DIR = "./files"

def ensure_files_dir():
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)
        print(f"Created directory: {FILES_DIR}")

def generate_file(filename="file10M.txt", lines=10_000_000):
    ensure_files_dir()
    filepath = os.path.join(FILES_DIR, filename)
    print(f"Generating {lines} random numbers into {filepath}...")
    with open(filepath, "w") as f:
        for _ in range(lines):
            f.write(f"{random.randint(0, 9999)}\n")
    print("File generation complete.\n")

def split_file(original_file, num_parts):
    ensure_files_dir()
    filepath = os.path.join(FILES_DIR, original_file)
    if not os.path.exists(filepath):
        print(f"{filepath} not found. Please generate it first.\n")
        return

    print(f"Splitting {original_file} into {num_parts} parts...")
    with open(filepath, "r") as f:
        lines = f.readlines()

    total = len(lines)
    chunk_size = total // num_parts

    for i in range(num_parts):
        part_lines = lines[i * chunk_size:(i + 1) * chunk_size] if i < num_parts - 1 else lines[i * chunk_size:]
        part_filename = os.path.join(FILES_DIR, f"part{i+1}.txt")
        with open(part_filename, "w") as part:
            part.writelines(part_lines)
        print(f"  -> Created {part_filename} with {len(part_lines)} lines.")

    print("File splitting complete.\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Generate file10M.txt (10 million lines)")
        print("2. Split into 2 parts")
        print("3. Split into 5 parts")
        print("4. Split into 10 parts")
        print("5. Split into 20 parts")
        print("6. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            generate_file()
        elif choice == "2":
            split_file("file10M.txt", 2)
        elif choice == "3":
            split_file("file10M.txt", 5)
        elif choice == "4":
            split_file("file10M.txt", 10)
        elif choice == "5":
            split_file("file10M.txt", 20)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
