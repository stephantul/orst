

class Heuristics(object):

    @staticmethod
    def brightness(rgb):
        """
        Simple brightness function

        :param rgb: a triple of ints, representing an RGB value.
        :return: A brightness value.
        """

        r, g, b = rgb
        return 0.2126*r + 0.7152*g + 0.0722*b

    @staticmethod
    def grayness(rgb):
        """
        Simple function to check if something is gray (with some margin)

        :param rgb: a triple of ints, representing an RGB value.
        :return: A boolean value if the pixel is gray
        """

        r, g, b = rgb
        return abs((int(r) - int(g)) < 5) and abs((int(r) - int(b)) < 5)

    @staticmethod
    def summation(rgb):

        return sum(rgb)

    @staticmethod
    def red(rgb):

        r, g, b = rgb
        return int(r) - (int(g) + int(b))

    @staticmethod
    def green(rgb):

        r, g, b = rgb
        return int(g) - (int(r) + int(b))

    @staticmethod
    def blue(rgb):

        r, g, b = rgb
        return int(b) - (int(g) + int(r))
