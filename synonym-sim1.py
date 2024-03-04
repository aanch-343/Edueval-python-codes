import spacy

nlp = spacy.load("en_core_web_lg")  # Change "en_core_web_sm" for different models

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    text1 = f1.read()
    text2 = f2.read()

doc1 = nlp(text1)
doc2 = nlp(text2)
print("Text of document 1:", doc1)
print("Text of document 2:", doc2)
print(doc1.similarity(doc2))
