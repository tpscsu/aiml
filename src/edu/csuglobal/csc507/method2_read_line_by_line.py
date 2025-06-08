import time


def main():
    start = time.time()

    with open("file1.txt", "r") as infile, open("newfile1_method2.txt", "w") as outfile:
        for line in infile:
            number = int(line.strip()) * 2
            outfile.write(f"{number}\n")

    end = time.time()
    print(f"Method 2 Execution Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
