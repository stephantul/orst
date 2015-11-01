import numpy as np
import cv2
import time
import logging


class Orst(object):

    def __init__(self):
        """
        Constructor. Creates three constants for use with the criteria.
        """

        self.BRIGHTVALUE = 60
        self.BLACKVALUE = 200
        self.WHITEVALUE = 380

    def sort(self, image, direction=u"row", criterium=u"bright", inverse=False):
        """
        Sorts an image by some heuristic, determined by the 'criterion' param.

        :param image: The image to sort, images are represented by 3D numpy matrices (x, y, colordepth).
        :param direction: The direction in which to sort, e.g. 'col' for column, 'row' for row.
        :param criterium: The criterium by which to sort.
        :param inverse: Whether to use the inverse of the criterium. Inverting a criterium means that, instead of
        sorting by X being below a value. The X must be higher or equal than the value.
        :return: the sorted image.
        """

        copy_image = np.copy(image)

        if direction == u"col":
            copy_image = np.rot90(copy_image, 1)
            self._sortbyrow(copy_image, criterium, inverse)
            copy_image = np.rot90(copy_image, 3)
        elif direction == u"row":
            self._sortbyrow(copy_image, criterium, inverse)
        else:
            raise ValueError(u"Incorrect type argument, should be 'row' or 'col'")

        return copy_image

    def _sortbyrow(self, image, criterium, inverse):
        """
        Sorts an image. Helper function to remove code duplication.

        :param image: The image to sort. Sorting is done in place.
        :param criterium: The criterium by which to sort.
        :param inverse: Whether to invert the sorting criterium
        """

        for row in image:

            if criterium == u"bright":
                self._sortline(row, self._brightness, self.BRIGHTVALUE, inverse)
            elif criterium == u"black":
                self._sortline(row, sum, self.BLACKVALUE, inverse)
            elif criterium == u"white":
                self._sortline(row, sum, self.WHITEVALUE, inverse)

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

    @staticmethod
    def _brightness(rgb):
        """
        Simple brightness function

        :param rgb: a triple of ints, representing an RGB value.
        :return: A brightness value.
        """

        r, g, b = rgb
        return 0.2126*r + 0.7152*g + 0.0722*b

if __name__ == u"__main__":

    logging.basicConfig(level=logging.INFO)

    path = u"test.jpg"

    img = cv2.imread(path, flags=-1)

    orst = Orst()
    img = orst.sort(img, direction=u"col", criterium=u"black", inverse=False)

    writepath = u"{0}-{1}.jpg".format(path.split(u".")[0], time.clock())

    cv2.imwrite(writepath, img)
    logging.log(level=logging.INFO, msg=u"Pyth is done!, wrote to {0}".format(writepath))
