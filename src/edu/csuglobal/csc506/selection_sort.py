def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        index_small = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[index_small]:
                index_small = j

        temp = numbers[i]
        numbers[i] = numbers [index_small]
        numbers[index_small] = temp


numbers = [10, 2, 78, 4, 45, 32, 7, 11]

print('UNSORTED:', numbers)

selection_sort(numbers)

print('SORTED:', numbers)