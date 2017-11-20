"""Heuristics for the sorting algorithm."""
import numpy as np

const_bright = np.array([.2126, .7152, .0722])[None, None, :]


def brightness(colors):
    """Calculate the brightness of a color."""
    return np.sum(colors * const_bright, -1)


def summation(colors):
    """Calculate sum of color triples."""
    return np.sum(colors, -1)
