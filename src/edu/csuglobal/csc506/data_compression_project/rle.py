def compress_rle(data: str) -> str:
    if not data:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1] and count < 99:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count:02}")
            count = 1
    compressed.append(f"{data[-1]}{count:02}")
    return ''.join(compressed)

def decompress_rle(data: str) -> str:
    decompressed = []
    i = 0
    while i < len(data):
        char = data[i]
        count = int(data[i + 1:i + 3])
        decompressed.append(char * count)
        i += 3
    return ''.join(decompressed)
