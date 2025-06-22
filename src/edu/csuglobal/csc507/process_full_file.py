import time

def main():
    start = time.time()
    with open("./files/file10M.txt", "r") as infile, open("./files/output_full.txt", "w") as outfile:
        for line in infile:
            number = int(line.strip()) * 2
            outfile.write(f"{number}\n")
    end = time.time()
    print(f"Sequential processing time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
