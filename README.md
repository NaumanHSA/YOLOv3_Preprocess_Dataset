# Multiscale retinex with color restoration

## Description
Python implementation of multiscale retinex with color restoration.

## Requirement
* Numpy
* OpenCV

## How to
Place test data into retinex_data folder and execute run.py.

## Reference
* [A multiscale retinex for bridging the gap between color images and the human observation of scenes] (http://ieeexplore.ieee.org/document/597272/)
* [An automated multi Scale Retinex with Color Restoration for image enhancement] (http://ieeexplore.ieee.org/document/6176791/)
* [Multiscale Retinex] (http://www.ipol.im/pub/art/2014/107/)


# Image Preprocessing for Efficient Training of YOLO Deep Learning Networks

## Description
Every artificial intelligence system needs big data for training. In particular, artificial intelligence for object detection requires a lot of images for training. It is possible to obtain training images from internet by web crawler. In most cases, however, images collected by the crawler are often not refined. In other words, it can't be used as training data in any artificial intelligence platform without proper pre-processing. We use cropped images each containing a single object that can be web-crawled directly. We call images having objects as Objects. Objects are relocated in new images which is similar to the environment (Base Images) in which the objects should be detected.

## Requirement
* Numpy
* OpenCV

## How to
Place objects data in objects, base images in base folder and execute pre_process_2.py.

## Reference
* [Image Preprocessing for Efficient Training of YOLO Deep Learning Networks] (https://ieeexplore.ieee.org/abstract/document/8367193/)
