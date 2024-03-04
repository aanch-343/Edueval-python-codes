from pytesseract import image_to_string
import cv2

def image_to_text(image_file, output_file):
    img = cv2.imread(image_file)

    # Preprocessing:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Thresholding

    # Optional deskewing (if needed):
    # deskewed = deskew(thresh)

    text = image_to_string(thresh, lang='eng', config='--psm 6')  # Use the preprocessed image

    with open(output_file, "w") as f:
        f.write(text)

if __name__ == "__main__":
    image_to_text("sample4.jpg", "output3.txt")
