import pytesseract
from PIL import Image


def read_content(images=None):
    # setting up tesseract path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    if images is None:
        header = Image.open('assets/header.jpg')
        content = Image.open('assets/content.jpg')
        total = Image.open('assets/total.jpg')

        imgs = [header, content, total]
    else:
        imgs = images

    # recognizing text
    txt = []
    for x, img in enumerate(imgs):
        text = pytesseract.image_to_string(img)
        with open('assets/ocr_text_' + str(x) + '.txt', 'w') as f:
            f.write(text)
        print(text)
        txt.append(text)

    return txt


if __name__ == '__main__':
    read_content()

