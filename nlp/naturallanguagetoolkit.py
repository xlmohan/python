# you need to install the nltk package first
import nltk
from nltk.tokenize import word_tokenize

# Download required resources (only once)
nltk.download('punkt')

text = "NLTK makes natural language processing easy!"
tokens = word_tokenize(text)

# Print the tokens in form of a list
print(tokens)
