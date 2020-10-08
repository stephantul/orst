"""Example with image."""
import logging
import numpy as np
from PIL import Image
from orst.orst import sort
from orst.reduction import summation

if __name__ == u"__main__":

    logging.basicConfig(level=logging.INFO)

    path = u"test.jpg"

    img = Image.open(path)
    o_img = np.array(img.getdata()).reshape((img.size[1], img.size[0], 3)) / 255

    def heuristic(x):
        return x < 0.9

    img = sort(o_img, heuristic, summation, num_rotations=1)
