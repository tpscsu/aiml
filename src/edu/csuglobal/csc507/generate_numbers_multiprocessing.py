from multiprocessing import Process
import random
import time


def write_to_file(start, end, file):
    with open(file, "a") as f:
        for _ in range(start, end):
            f.write(f"{random.randint(0, 32767)}\n")


if __name__ == '__main__':
    start_time = time.time()

    processes = []
    chunk_size = 250_000
    for _ in range(4):
        p = Process(target=write_to_file, args=(0, chunk_size, "file2.txt"))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time:.2f} seconds")
