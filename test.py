#!usr/bin/env python
# @Author:	Suhas Kashyap
# @Date:	2017-03-22

# test file

from utils import *

img = read_img('files/500.jpg')

img = img_to_gray(img)
#img = img_to_neg(img)
#img = binarize(img, 128)
#img = sobel_edge(img, 'h')
histogram(img)
fourier(img)

display('image', img)