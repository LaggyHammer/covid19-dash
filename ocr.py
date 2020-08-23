import pytesseract
from PIL import Image
from image_processing import get_black_and_white


def read_image(image=None):
    # setting up tesseract path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    if image is None:
        img = Image.open('assets/img_bw.jpg')
    else:
        img = image

    # recognizing text
    text = pytesseract.image_to_string(img)
    print(text)

    return text


if __name__ == '__main__':
    read_image()
