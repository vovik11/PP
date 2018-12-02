import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image, ImageEnhance


def show_image():
    image = mpimg.imread('image.jpg')
    plt.imshow(image)
    plt.show()


def channel():
    image = mpimg.imread('image.jpg')
    ired, iblue, igreen = image.copy(), image.copy(), image.copy()
    ired[:,:, 1], ired[:, :, 2] = 0, 0
    plt.imshow(ired)
    plt.show()
    iblue[:, :, 0], iblue[:, :, 1] = 0, 0
    plt.imshow(iblue)
    plt.show()
    igreen[:, :, 0], igreen[:, :, 2] = 0, 0
    plt.imshow(igreen)
    plt.show()
    img =  Image.open('image.jpg')
    r, g, b = img.split()
    r.show()
    g.show()
    b.show()


def contrast():
    img =  Image.open('image.jpg')
    img1 = img.copy()
    img = ImageEnhance.Contrast(img).enhance(0.1)
    img.show()
    img1 = ImageEnhance.Contrast(img1).enhance(50.0)
    img1.show()


def gray_image():
    rgb = mpimg.imread('image.jpg')
    gray = np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    plt.show()


if __name__ == "__main__":
    show_image()
    contrast()
    channel()
    gray_image()
