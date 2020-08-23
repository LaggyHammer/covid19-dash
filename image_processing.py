import cv2
import os


def get_black_and_white(path, image):

    original_image = cv2.imread(image)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(path, 'img_bw.jpg'), blackAndWhiteImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return blackAndWhiteImage


def get_content(image, path='assets'):
    header = image[45:75, 10:685]
    content = image[115:1005, 10:685]
    total = image[1035:1060, 10:685]

    cv2.imwrite(os.path.join(path, 'header.jpg'), header)
    cv2.imwrite(os.path.join(path, 'content.jpg'), content)
    cv2.imwrite(os.path.join(path, 'total.jpg'), total)

    return [header, content, total]


if __name__ == '__main__':

    bw_image = get_black_and_white("assets", 'assets/COVID1.JPG')
    get_content(bw_image)
