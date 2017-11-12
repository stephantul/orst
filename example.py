"""Example with image."""
import logging
import numpy as np
from PIL import Image
from orst.orst import sort
from orst.heuristic import brightness

if __name__ == u"__main__":

    logging.basicConfig(level=logging.INFO)

    path = u"orst/test.jpg"

    img = Image.open(path)
    o_img = np.array(img.getdata()).reshape((img.size[1], img.size[0], 3)) / 255

    simple_comp = lambda x: x > .4
    img = sort(o_img, simple_comp)