import matplotlib.image as mpimg
import numpy as np

def color2grayscale(vector):
    return vector[0]*0.3 + vector[1]*0.59 + vector[2]*0.11

def convert_to_gray():
    img = mpimg.imread('dog.jpeg')
    gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
    gray_img_01[0 , 0]

if __name__ == '__main__':
    convert_to_gray()