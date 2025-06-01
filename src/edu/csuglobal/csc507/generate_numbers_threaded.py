import random
import threading
import time


def write_random(start, end, file):
    with open(file, "a") as f:
        for _ in range(start, end):
            f.write(f"{random.randint(0, 32767)}\n")


start = time.time()

threads = []
chunk = 250_000
for i in range(4):
    t = threading.Thread(target=write_random, args=(0, chunk, "file2.txt"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Threaded execution time: {end - start:.2f} seconds")
