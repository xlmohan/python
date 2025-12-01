# Using range with increment
for i in range(0, 10, 1):
    print(i)

# Incrementing by 2
for i in range(0, 10, 2):
    print(i)

# Decrementing
for i in range(10, 0, -1):
    print(i)

# Manual increment in loop
i = 0
for _ in range(5):
    print(f"Pre-increment: {i}")
    i += 1

# Simulating post-increment behavior
i = 0
for _ in range(5):
    print(f"Post-increment: {i}")
    i += 1