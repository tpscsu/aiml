import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", "char freq left right")):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [Node(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged = Node(None, n1.freq + n2.freq, n1, n2)
        heapq.heappush(heap, merged)
    return heap[0]

def generate_codes(node, prefix='', code_map={}):
    if node.char is not None:
        code_map[node.char] = prefix
    else:
        generate_codes(node.left, prefix + '0', code_map)
        generate_codes(node.right, prefix + '1', code_map)
    return code_map

def encode_huffman(data):
    tree = build_huffman_tree(data)
    codes = generate_codes(tree)
    encoded = ''.join(codes[char] for char in data)
    return encoded, tree

def decode_huffman(encoded, tree):
    result = []
    node = tree
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            result.append(node.char)
            node = tree
    return ''.join(result)