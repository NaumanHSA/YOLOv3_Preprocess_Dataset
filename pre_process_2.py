import glob, os
from PIL import Image
import cv2
import errno
import sys

# ============================== Config ========================================

DATA_PATH_BG = './base_images'
DATA_PATH_FG = './objects'
OUTPUT_PATH = './output_images'
TEST_PERCENTAGE = 15  # Test Image Percentage
IMAGE_FORMAT = 'jpg'  # Image Format of your data [jpg / png / jpeg]
ANNOTATION_CLASS = '0'


# ============================== Config ========================================


def __convert__(min_x, min_y, max_x, max_y, image_width, image_height, basename):
    try:
        norm_width = (max_x - min_x) / image_width
        norm_height = (max_y - min_y) / image_height

        norm_x = (((max_x - min_x) / 2) + min_x) / image_width
        norm_y = (((max_y - min_y) / 2) + min_y) / image_height

        new_file = open(str(OUTPUT_PATH) + '/' + basename + '.txt', "a+")
        new_file.write(ANNOTATION_CLASS + ' ' + str(norm_x) + ' ' + str(norm_y) + ' ' + str(norm_width) + ' ' + str(
            norm_height) + '\n')
        new_file.close()

    except Exception as e:
        print(e)


def process():
    FG_list = []
    counter = 0

    for pathAndFilename_fg in glob.iglob(os.path.join(DATA_PATH_FG, "*." + IMAGE_FORMAT)):
        FG_list.append(pathAndFilename_fg)

    for pathAndFilename_bg in glob.iglob(os.path.join(DATA_PATH_BG, "*." + IMAGE_FORMAT)):
        basename = os.path.basename(pathAndFilename_bg)
        image_bg = Image.open(pathAndFilename_bg)
        bg_w, bg_h = image_bg.size

        if counter >= len(FG_list):
            counter = 0

        icon_1 = Image.open(FG_list[counter])
        counter += 1
        icon_2 = Image.open(FG_list[counter])
        counter += 1
        icon_3 = Image.open(FG_list[counter])
        counter += 1

        fg_w, fg_h = icon_1.size
        image_bg.paste(icon_1, (fg_w, fg_h, fg_w * 2, fg_h * 2))
        __convert__(fg_w, fg_h, fg_w * 2, fg_h * 2, bg_w, bg_h, basename.split('.')[0])

        fg_w, fg_h = icon_2.size
        image_bg.paste(icon_2, (bg_w - (2 * fg_w), fg_h, bg_w - fg_w, fg_h * 2))
        __convert__(bg_w - (2 * fg_w), fg_h, bg_w - fg_w, fg_h * 2, bg_w, bg_h, basename.split('.')[0])

        fg_w, fg_h = icon_3.size
        image_bg.paste(icon_3, (int(bg_w / 2), bg_h - (2 * fg_h), int(bg_w / 2) + fg_w, bg_h - fg_h))
        __convert__(int(bg_w / 2), bg_h - (2 * fg_h), int(bg_w / 2) + fg_w, bg_h - fg_h, bg_w, bg_h,
                    basename.split('.')[0])

        image_bg.save(os.path.join(OUTPUT_PATH, basename), "JPEG")


def image_resize(image, new_width=None, new_height=None):
    dim = None
    image = cv2.imread(image)
    (img_w, img_h) = image.shape[:2]

    if img_w > img_h:
        img_h = int((new_width * img_h) / img_w)
        dim = (new_width, img_h)
    else:
        img_w = int((new_height * img_w) / img_h)
        dim = (img_w, new_height)

    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def resize_images(DATA_PATH, x, y):
    for pathAndFilename in glob.iglob(os.path.join(DATA_PATH, "*." + IMAGE_FORMAT)):
        basename = os.path.basename(pathAndFilename)

        new_image = image_resize(pathAndFilename, x, y)
        cv2.imwrite(os.path.join(OUTPUT_PATH, basename), new_image)


# resize_images(DATA_PATH_BG, 60, 60)
process()
