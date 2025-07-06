import time

start = time.time()
with open('./files/module8/hugefile1.txt') as f1, open('./files/module8/hugefile2.txt') as f2:
    for _ in range(500_000_000):
        next(f1)
        next(f2)
    with open('./files/module8/second_half_output.txt', 'w') as fout:
        for line1, line2 in zip(f1, f2):
            fout.write(f"{int(line1.strip()) + int(line2.strip())}\n")

end = time.time()
print(f"Second half time: {end - start:.2f} seconds")
