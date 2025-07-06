import os

def split_file(input_path, lines_per_file, output_prefix, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    part = 0
    line_count = 0
    output_path = os.path.join(output_dir, f"{output_prefix}_{part:02d}.txt")
    fout = open(output_path, "w")

    with open(input_path, 'r') as fin:
        for line in fin:
            fout.write(line)
            line_count += 1
            if line_count >= lines_per_file:
                fout.close()
                part += 1
                line_count = 0
                output_path = os.path.join(output_dir, f"{output_prefix}_{part:02d}.txt")
                fout = open(output_path, "w")

    fout.close()
    print(f"Split complete: {part + 1} parts created in '{output_dir}'.")

def main():
    input_file = "./files/module8/hugefile2.txt"
    lines_per_file = 100_000_000
    output_prefix = "hugefile2_part"
    output_dir = "./files/module8"

    split_file(input_file, lines_per_file, output_prefix, output_dir)

if __name__ == "__main__":
    main()
