# First-Fit Algorithm
def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    blocks = block_sizes.copy()
    for pid, process in enumerate(process_sizes):
        for bid, block in enumerate(blocks):
            if block >= process:
                allocation[pid] = bid
                blocks[bid] -= process
                break
    print("First-Fit Allocation Results:")
    for pid, block_id in enumerate(allocation):
        if block_id != -1:
            print(f"Process {pid + 1} of size {process_sizes[pid]} KB -> Block {block_id + 1}")
        else:
            print(f"Process {pid + 1} of size {process_sizes[pid]} KB -> Not Allocated")
    print("\n")


# Best-Fit Algorithm
def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    blocks = block_sizes.copy()
    for pid, process in enumerate(process_sizes):
        best_index = -1
        for bid, block in enumerate(blocks):
            if block >= process:
                if best_index == -1 or blocks[bid] < blocks[best_index]:
                    best_index = bid
        if best_index != -1:
            allocation[pid] = best_index
            blocks[best_index] -= process
    print("Best-Fit Allocation Results:")
    for pid, block_id in enumerate(allocation):
        if block_id != -1:
            print(f"Process {pid + 1} of size {process_sizes[pid]} KB -> Block {block_id + 1}")
        else:
            print(f"Process {pid + 1} of size {process_sizes[pid]} KB -> Not Allocated")
    print("\n")


# Main Execution
if __name__ == "__main__":
    memory_blocks = [100, 500, 200, 300, 600]
    process_sizes = [212, 417, 112, 426]
    print("Memory Blocks:", memory_blocks)
    print("Process Sizes:", process_sizes)
    print("=" * 50)
    first_fit(memory_blocks, process_sizes)
    best_fit(memory_blocks, process_sizes)
