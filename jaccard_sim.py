def file_to_tokens(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        tokens = set(text.split())  # Split text into tokens (words) and convert to set for uniqueness
    return tokens

def calculate_jaccard_similarity(file1_path, file2_path):
    # Get tokens from both files
    tokens1 = file_to_tokens(file1_path)
    tokens2 = file_to_tokens(file2_path)
    
    # Calculate Jaccard similarity
    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))
    similarity = intersection / union if union > 0 else 0
    
    return similarity

if __name__ == "__main__":
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    similarity = calculate_jaccard_similarity(file1_path, file2_path)
    print("Jaccard Similarity between the two files:", similarity)
