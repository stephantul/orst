"""Line sorting."""
import numpy as np


from .reduction import brightness


def multisort(image, params):
    """Sort an image by performing multiple transforms sequentially."""
    for x in params:
        image = sort(image, **x)

    return image


def sort(image, heuristic, reduction=brightness, num_rotations=0, copy=True):
    """Sort an image by some heuristic."""
    num_rotations = num_rotations % 4
    if copy:
        image = np.copy(image)
    if num_rotations:
        image = np.rot90(image, k=num_rotations)

    reduced = reduction(image)
    padding = np.zeros((reduced.shape[0], 1)) + heuristic(0)
    m = heuristic(np.concatenate([padding, reduced, padding], axis=1))

    d = np.diff(m.astype(np.int))
    s = np.where(d > 0)
    e = np.where(d < 0)

    for line, start, length in zip(s[0], s[1], e[1] - s[1]):
        end = start + length
        segment = image[line, start:end]
        sort = np.argsort(reduced[line, start:end])
        segment[:] = segment[sort]

    if num_rotations:
        image = np.rot90(image, k=4 - num_rotations)

    return image
