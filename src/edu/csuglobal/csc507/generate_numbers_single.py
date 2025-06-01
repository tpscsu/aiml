import random
import time

start = time.time()

with open("file2.txt", "w") as f:
    for _ in range(1_000_000):
        f.write(f"{random.randint(0, 32767)}\n")

end = time.time()
print(f"Execution time: {end - start:.2f} seconds")
