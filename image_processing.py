import cv2
import os
from covid_scrapping import get_update


def get_black_and_white(path, image):

    original_image = cv2.imread(image)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(path, 'img_bw.jpg'), blackAndWhiteImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return blackAndWhiteImage


if __name__ == '__main__':

    bw_image = get_black_and_white("assets", 'assets/COVID1.JPG')
