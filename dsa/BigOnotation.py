def time_complexity_example(n):
    total = 0
    for i in range(n):          # O(n)
        for j in range(n):      # O(n)
            total += 1          # O(1)
    return total                # Overall: O(n^2)