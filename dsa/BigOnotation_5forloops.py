def five_for_loops(n):
    count = 0
    for i in range(n):          # O(n)
        for j in range(n):      # O(n)
            for k in range(n):  # O(n)
                for l in range(n):  # O(n)
                    for m in range(n):  # O(n)
                        count += 1      # O(1)
    return count                # Overall: O(n^5)