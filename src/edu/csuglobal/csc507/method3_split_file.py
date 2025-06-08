import time


def process_chunk(start_line, num_lines, input_file, output_file):
    with open(input_file, "r") as infile:
        lines = infile.readlines()[start_line:start_line + num_lines]
    doubled = [str(int(line.strip()) * 2) for line in lines]
    with open(output_file, "a") as outfile:
        outfile.writelines(f"{n}\n" for n in doubled)


def main():
    start = time.time()

    with open("file1.txt") as f:
        total_lines = sum(1 for _ in f)

    half = total_lines // 2
    process_chunk(0, half, "file1.txt", "newfile1_method3.txt")
    process_chunk(half, total_lines - half, "file1.txt", "newfile1_method3.txt")

    end = time.time()
    print(f"Method 3 Execution Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
