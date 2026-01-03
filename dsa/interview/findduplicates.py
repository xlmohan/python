numbers = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 5]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"Duplicate found: {numbers[i]} at indices {i} and {j}")
            break