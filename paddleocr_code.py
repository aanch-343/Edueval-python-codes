from paddleocr import PaddleOCR

ocr = PaddleOCR() # need to run only once to download and load model into memory

# Read image
img_path = 'sample4.jpg'
result = ocr.ocr(img_path)

# Write recognized text to a text file
output_file = 'recognized_text.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for line in result:
        f.write(' '.join([word[1][0] for word in line]) + '\n')

print("Recognized text saved to:", output_file)
