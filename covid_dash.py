from covid_scrapping import *
from image_processing import *
from ocr import *


def main():

    update_image = get_update("http://www.rajswasthya.nic.in/", "assets")
    bw_image = get_black_and_white("assets", update_image)
    seg_images = get_content(bw_image)
    content_text = read_content(seg_images)
