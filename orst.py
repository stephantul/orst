#  -*- coding: utf-8 -*-

import numpy as np
import cv2
import time
import logging
from heuristic import Heuristics


class Orst(object):

    def multisort(self, image, listargs=()):

        original = np.copy(image)

        output = np.copy(image)

        for args in listargs:

            heuristic, condition, inverse, nrturns = args
            temp = self.sort(original, heuristic, condition, inverse, nrturns) - original

            output = np.where(output != 0, temp, output)

        return output

    def sort(self, image, heuristic, condition, inverse, nrturns=0):
        """
        Sorts an image by some heuristic, determined by the 'criterion' param.

        :param image: The image to sort, images are represented by 3D numpy matrices (x, y, colordepth).
        :param heuristic: the function to use for sorting.
        :param condition: the condition to start sorting. Closely tied to the heuristic used.
        :param inverse: Whether to use the inverse of the heuristic. Inverting a criterium means that, instead of
        sorting by X being below a value. The X must be higher or equal than the value.
        :return: the sorted image.
        """

        copy_image = np.copy(image)

        if nrturns > 0:
            nrturns %= 4
            copy_image = np.rot90(copy_image, nrturns)

        for line in copy_image:
            self._sortline(line, heuristic, condition, inverse)

        if nrturns > 0:
            copy_image = np.rot90(copy_image, 4 - nrturns)

        return copy_image

    @staticmethod
    def _sortline(line, function, constant, inverse):
        """
        Sorts a line by comparing function(pixel) to constant for each pixel in a line.

        :param line: The line to sort.
        :param function: The function to use for sorting.
        :param constant: The constant used to compare the pixels to.
        :param inverse: Whether to invert the sorting criterium.
        """

        active = False
        start = 0

        for idx, val in enumerate(line):

            if active:
                if not(inverse and function(val) >= constant) and (inverse or function(val) >= constant):
                    continue
                else:
                    end = idx
                    line[start:end] = np.sort(line[start:end], axis=0)
                    active = False
            elif not active:
                if not(inverse and function(val) >= constant) and (inverse or function(val) >= constant):
                    active = True
                    start = idx


if __name__ == u"__main__":

    logging.basicConfig(level=logging.INFO)

    path = u"test.jpg"

    img = cv2.imread(path, flags=-1)

    orst = Orst()

    img = orst.sort(img, Heuristics.summation, 200, True, nrturns=1)

    writepath = u"{0}-{1}.jpg".format(path.split(u".")[0], time.clock())

    cv2.imwrite(writepath, img)
    logging.log(level=logging.INFO, msg=u"orst is done!, wrote to {0}".format(writepath))
