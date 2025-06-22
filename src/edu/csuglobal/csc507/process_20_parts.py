import multiprocessing
import time

def process_file(infile, outfile):
    with open(infile, "r") as f_in, open(outfile, "w") as f_out:
        for line in f_in:
            f_out.write(f"{int(line.strip()) * 2}\n")

def main():
    start = time.time()
    parts = [f"./files/part{i}.txt" for i in range(1, 21)]
    outputs = [f"./files/out{i}.txt" for i in range(1, 21)]

    processes = []
    for i in range(20):
        p = multiprocessing.Process(target=process_file, args=(parts[i], outputs[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    with open("./files/output_20parts.txt", "w") as f_out:
        for fname in outputs:
            with open(fname, "r") as f_in:
                f_out.writelines(f_in.readlines())

    end = time.time()
    print(f"20-part parallel processing time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
