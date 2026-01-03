import pandas as pd
import numpy as np
import re
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
nltk.download('punkt')
from nltk.tokenize import word_tokenize
def vectorize_texts(texts, method='count'):
    """
    Vectorizes a list of texts using the specified method.
    
    Parameters:
    texts (list of str): The texts to vectorize.
    method (str): The vectorization method to use ('count' or 'tfidf').
    
    Returns:
    sparse matrix: The vectorized representation of the texts.
    """
    if method == 'count':
        vectorizer = CountVectorizer(tokenizer=word_tokenize)
    elif method == 'tfidf':
        vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    else:
        raise ValueError("Method must be 'count' or 'tfidf'")
    
    vectors = vectorizer.fit_transform(texts)
    return vectors