def merge_sort(records):
    if len(records) <= 1:
        return records
    mid = len(records) // 2
    left_half = merge_sort(records[:mid])
    right_half = merge_sort(records[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

def main():
    patient_records = ["Taylor", "Smith", "Johnson", "Lee", "Brown", "Davis", "Adams"]
    print("Original Records:")
    print(patient_records)

    sorted_records = merge_sort(patient_records.copy())
    print("\nSorted Records (Merge Sort):")
    print(sorted_records)

if __name__ == "__main__":
    main()
