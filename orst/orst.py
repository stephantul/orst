"""Line sorting."""
import numpy as np


from .heuristic import brightness


def multisort(image, params):
    """Sort an image by performing multiple transforms sequentially."""
    for x in params:
        comparer = x['comparer']
        heuristic = x['heuristic']
        num_rotations = x['num_rotations']
        image = sort(image, comparer, heuristic, num_rotations)

    return image


def sort(image, comparer, heuristic=brightness, num_rotations=0):
    """Sort an image by some heuristic."""
    num_rotations = num_rotations % 4
    image = np.copy(image)
    if num_rotations:
        image = np.rot90(image, k=num_rotations)

    mask = heuristic(image)
    a = np.zeros((mask.shape[0], 1)) + comparer(0)
    m = comparer(np.concatenate([a, mask, a], axis=1))

    d = np.diff(m.astype(np.int))
    s = np.where(d > 0)
    e = np.where(d < 0)

    for line, start, length in zip(s[0], s[1], e[1] - s[1]):
        end = start + length
        segment = image[line, start:end]
        sort = np.argsort(mask[line, start:end])
        segment[:] = segment[sort]

    if num_rotations:
        image = np.rot90(image, k=4 - num_rotations)

    return image
