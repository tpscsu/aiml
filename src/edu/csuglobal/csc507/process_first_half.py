import time

def read_half(file_path, stop_line):
    with open(file_path) as f:
        for i, line in enumerate(f):
            if i >= stop_line:
                break
            yield line.strip()

start = time.time()
f1 = read_half('./files/module8/hugefile1.txt', 500_000_000)
f2 = read_half('./files/module8/hugefile2.txt', 500_000_000)

with open('./files/module8/first_half_output.txt', 'w') as fout:
    for l1, l2 in zip(f1, f2):
        fout.write(f"{int(l1) + int(l2)}\n")

end = time.time()
print(f"First half time: {end - start:.2f} seconds")
