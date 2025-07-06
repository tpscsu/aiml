import time

def main():
    start = time.time()
    with open('./files/module8/hugefile1.txt') as f1, \
            open('./files/module8/hugefile2.txt') as f2, \
            open('files/module8/totalfile_1.txt', 'w') as fout:
        for line1, line2 in zip(f1, f2):
            total = int(line1.strip()) + int(line2.strip())
            fout.write(f"{total}\n")
    end = time.time()
    print(f"Sequential processing time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
