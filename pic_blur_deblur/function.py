import cv2

import numpy.matlib
import numpy as np
from scipy import sparse as sp


def blur(img, count = 10, var1 = 1/4, var2 = 1/2, var3 = 1/4):
    v = [var1, var2, var3]
    diags = np.array([-1, 0, 1])
    B = sp.diags(v, diags, shape=(img.shape[0], img.shape[0]))
    C = sp.diags(v, diags, shape=(img.shape[1], img.shape[1]))
    img_B = numpy.power(B, count) * img
    img_C= img* numpy.power(C, count)
    img_blur = img_B * numpy.power(C, count)
    img_B = img_B.astype(np.uint8)
    img_C = img_C.astype(np.uint8)
    img_blur = img_blur.astype(np.uint8)
    return img_blur, img_B, img_C


def cus_filter2D(image, a11 = 0, a12 = -1, a13 = 0, a21 = -1, a22 = 5, a23 = -1,
                     a31 = 0, a32 = -1, a33 = 0):
    kernel = np.array([[a11, a12, a13],
                       [a21, a22, a23],
                       [a31, a32, a33]],
                      np.float32)  # 默认锐化
    return cv2.filter2D(image, -1, kernel=kernel)

