import sys

def process_file(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2, open(output_path, 'w') as fout:
        for line1, line2 in zip(f1, f2):
            total = int(line1.strip()) + int(line2.strip())
            fout.write(f"{total}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 process_pair.py <file1> <file2> <output>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = sys.argv[3]

    process_file(file1, file2, output)
