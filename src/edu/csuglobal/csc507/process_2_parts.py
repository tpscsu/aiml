import multiprocessing
import time

def process_file(infile, outfile):
    with open(infile, "r") as f_in, open(outfile, "w") as f_out:
        for line in f_in:
            f_out.write(f"{int(line.strip()) * 2}\n")

def main():
    start = time.time()
    p1 = multiprocessing.Process(target=process_file, args=("./files/part1.txt", "./files/out1.txt"))
    p2 = multiprocessing.Process(target=process_file, args=("./files/part2.txt", "./files/out2.txt"))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    with open("./files/output_2parts.txt", "w") as outfile:
        for part in ["./files/out1.txt", "./files/out2.txt"]:
            with open(part, "r") as f:
                outfile.writelines(f.readlines())

    end = time.time()
    print(f"2-part parallel processing time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
