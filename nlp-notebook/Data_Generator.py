import random

# Sample names and words to use
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"]
words = ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "house", "ice", "jungle"]

# Open a file to write
with open("synthetic_data.tsv", "w", encoding="utf-8") as f:
    for i in range(1, 5001):  # 5000 lines
        name = random.choice(names)
        # Create a random sentence of 5–10 words
        random_text = " ".join(random.choices(words, k=random.randint(5, 10)))
        # Write tab-separated values
        f.write(f"{i}\t{name}\t{random_text}\n")