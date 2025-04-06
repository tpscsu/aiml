def bubble_sort(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if records[j] > records[j + 1]:
                records[j], records[j + 1] = records[j + 1], records[j]
    return records

def main():
    patient_records = ["Taylor", "Smith", "Johnson", "Lee", "Brown", "Davis", "Adams"]
    print("Original Records:")
    print(patient_records)

    sorted_records = bubble_sort(patient_records.copy())
    print("\nSorted Records (Bubble Sort):")
    print(sorted_records)

if __name__ == "__main__":
    main()
