import re #regular expressions module
def tokenize(text):
    # Use regular expressions to find words and punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    return tokens

# Example usage
sample_text = "Hello, world! This is a test."
print(tokenize(sample_text))