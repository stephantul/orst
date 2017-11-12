"""Line sorting."""
import numpy as np


from .heuristic import brightness


def sort(image, comparer, heuristic=brightness):
    """Sort an image by some heuristic."""
    mask = heuristic(image)
    a = np.zeros((mask.shape[0], 1))
    m = comparer(np.concatenate([a, mask, a], axis=1))

    d = np.diff(m.astype(np.int))
    s = np.where(d > 0)
    e = np.where(d < 0)

    for line, start, length in zip(s[0], s[1], e[1] - s[1]):
        end = start + length
        segment = image[line, start:end]
        sort = np.argsort(mask[line, start:end])
        segment[:] = segment[sort]

    return image
