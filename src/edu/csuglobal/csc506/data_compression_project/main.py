import time
from rle import compress_rle, decompress_rle
from huffman import encode_huffman, decode_huffman

TEST_FILES = {
    "short_text": "test_inputs/short_text.txt",
    "long_repetitive": "test_inputs/long_repetitive.txt",
    "mixed_text": "test_inputs/mixed_text.txt"
}

def run_rle(label, path):
    print(f"\n--- RLE Compression for {label} ---")
    try:
        with open(path, 'r') as f:
            original = f.read()

        start = time.time()
        compressed = compress_rle(original)
        end = time.time()

        decompressed = decompress_rle(compressed)
        assert decompressed == original, "RLE Decompression failed!"

        ratio = len(compressed) / len(original) if original else 0
        print(f"Compression Ratio: {ratio:.3f}")
        print(f"Time Taken: {end - start:.4f} seconds")
        print("Decompression successful ✅")

    except AssertionError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Error during RLE compression: {e}")

def run_huffman(label, path):
    print(f"\n--- Huffman Compression for {label} ---")
    try:
        with open(path, 'r') as f:
            original = f.read()

        start = time.time()
        encoded, tree = encode_huffman(original)
        end = time.time()

        decoded = decode_huffman(encoded, tree)
        assert decoded == original, "Huffman Decompression failed!"

        bits = len(encoded)
        ratio = bits / (len(original) * 8) if original else 0
        print(f"Compression Ratio: {ratio:.3f} (compared to 8 bits/char)")
        print(f"Time Taken: {end - start:.4f} seconds")
        print("Decompression successful ✅")

    except AssertionError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Error during Huffman compression: {e}")

def main():
    for label, path in TEST_FILES.items():
        run_rle(label, path)
        run_huffman(label, path)

if __name__ == "__main__":
    main()
