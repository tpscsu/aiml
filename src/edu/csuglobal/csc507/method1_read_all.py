import time


def main():
    start = time.time()

    with open("file1.txt", "r") as f:
        numbers = [int(line.strip()) * 2 for line in f]

    with open("newfile1_method1.txt", "w") as f:
        f.writelines(f"{n}\n" for n in numbers)

    end = time.time()
    print(f"Method 1 Execution Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
