import re
from sklearn.feature_extraction.text import TfidfVectorizer
# Preprocessing function (optional)
def preprocess_text(text):
  """
  Preprocesses text by performing lowercase conversion, optional special character removal,
  and optional stop word removal.

  Args:
    text: The text to preprocess (string).

  Returns:
    The preprocessed text (string).
  """

  text = text.lower()

  # Uncomment the following line if you want to remove special characters
  # text = re.sub(r"[^\w\s]", "", text)

  # Uncomment the following lines if you want to remove stop words
  # stop_words = ["a", "an", "the", "is", "of", "to", "and", "in", "on", "for"]
  # text = " ".join([word for word in text.split() if word not in stop_words])

  return text

# Cosine similarity function
def cosine_similarity(text1, text2):
  """
  Calculates the cosine similarity between two text strings.

  Args:
    text1: The first text string.
    text2: The second text string.

  Returns:
    The cosine similarity score between the two texts.
  """

  # Optionally preprocess the text
  # text1 = preprocess_text(text1)
  # text2 = preprocess_text(text2)

  # Create TF-IDF vectors
  vectorizer = TfidfVectorizer()
  vectors = vectorizer.fit_transform([text1, text2])

  # Check for dimension mismatch
  if vectors.shape[1] != len(vectorizer.vocabulary_):
    print("Warning: Potential vocabulary mismatch. Consider increasing max_features in TfidfVectorizer or using lemmatization/stemming.")

  # Calculate cosine similarity
  similarity = vectors[0].dot(vectors[1]) / (vectors[0].norm() * vectors[1].norm())

  return similarity

# Example usage
text1 = "computer electronic device"
text2 = "computer is an electronic device"

similarity = cosine_similarity(text1, text2)
print(f"Cosine similarity: {similarity}")
