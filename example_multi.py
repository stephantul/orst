"""Example with image."""
import logging
import numpy as np
from PIL import Image
from orst.orst import multisort
from orst.reduction import brightness, summation

if __name__ == u"__main__":

    logging.basicConfig(level=logging.INFO)

    path = u"test.jpg"

    img = Image.open(path)
    o_img = np.array(img.getdata()).reshape((img.size[1], img.size[0], 3)) / 255

    params = [
        {"heuristic": lambda x: x < 0.4, "reduction": brightness, "num_rotations": 2},
        {"heuristic": lambda x: x > 0.3, "reduction": summation, "num_rotations": 1},
    ]

    img = multisort(o_img, params)
