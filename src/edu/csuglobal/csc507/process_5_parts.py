import multiprocessing
import time

def process_file(infile, outfile):
    with open(infile, "r") as f_in, open(outfile, "w") as f_out:
        for line in f_in:
            f_out.write(f"{int(line.strip()) * 2}\n")

def main():
    start = time.time()
    parts = ["./files/part1.txt", "./files/part2.txt", "./files/part3.txt", "./files/part4.txt", "./files/part5.txt"]
    output_parts = ["./files/out1.txt", "./files/out2.txt", "./files/out3.txt", "./files/out4.txt", "./files/out5.txt"]

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=process_file, args=(parts[i], output_parts[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    with open("./files/output_5parts.txt", "w") as f_out:
        for fname in output_parts:
            with open(fname, "r") as f_in:
                f_out.writelines(f_in.readlines())

    end = time.time()
    print(f"5-part parallel processing time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
