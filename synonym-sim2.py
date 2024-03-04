import spacy
from nltk.corpus import wordnet as wn

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def get_synonyms(word):
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def file_to_tokens(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        doc = nlp(text)
        tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def calculate_similarity(file1_path, file2_path):
    # Get tokens from both files
    tokens1 = file_to_tokens(file1_path)
    tokens2 = file_to_tokens(file2_path)
    
    # Get synonyms for each token
    synonyms1 = set()
    synonyms2 = set()
    for token in tokens1:
        synonyms = get_synonyms(token)
        synonyms1.update(synonyms)
    for token in tokens2:
        synonyms = get_synonyms(token)
        synonyms2.update(synonyms)
    
    # Calculate similarity using Jaccard similarity
    intersection = len(synonyms1.intersection(synonyms2))
    union = len(synonyms1.union(synonyms2))
    similarity = intersection / union if union > 0 else 0
    
    return similarity

if __name__ == "__main__":
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    similarity = calculate_similarity(file1_path, file2_path)
    print("Similarity between the two files:", similarity)
