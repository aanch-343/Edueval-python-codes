import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(text_file1_path, text_file2_path):
    """
    Calculates the cosine similarity between two text files.

    Args:
        text_file1_path: Path to the first text file.
        text_file2_path: Path to the second text file.

    Returns:
        The cosine similarity score between the text files.
    """

    # Read text files
    with open(text_file1_path, 'r', encoding='utf-8') as f1:
        text1 = f1.read()
    with open(text_file2_path, 'r', encoding='utf-8') as f2:
        text2 = f2.read()

    # Preprocess text (optional)
    # - Lowercase
    text1 = text1.lower()
    text2 = text2.lower()

    # - Remove special characters (optional)
    import re
    text1 = re.sub(r"[^\w\s]", "", text1)
    text2 = re.sub(r"[^\w\s]", "", text2)

    # - Lemmatization or stemming (optional)
    # from nltk.stem import PorterStemmer
    # stemmer = PorterStemmer()
    # text1 = " ".join([stemmer.stem(word) for word in text1.split()])
    # text2 = " ".join([stemmer.stem(word) for word in text2.split()])

    # - Stop word removal (optional)
    stop_words = ["a", "an", "the", "is", "of", "to", "and", "in", "on", "for"]
    text1 = " ".join([word for word in text1.split() if word not in stop_words])
    text2 = " ".join([word for word in text2.split() if word not in stop_words])

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(max_features=1000)  # Adjust as needed
    vectors = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return similarity


# Example usage
text_file1_path = "file1.txt"  # Replace with your actual path
text_file2_path = "file2.txt"  # Replace with your actual path

similarity = calculate_cosine_similarity(text_file1_path, text_file2_path)

print("Cosine similarity:", similarity)
res=(similarity/1)*10
print(res)
