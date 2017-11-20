import cv2
import numpy as np
from orst import sort, multisort
from orst import brightness


if __name__ == "__main__":

    simple_comp = lambda x: x > 100

    num_frames = 150
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 20, frame.shape[:-1][::-1])

    resultant_frames = []

    for x in range(num_frames):

        print(x)

        ret, frame = cam.read()
        if ret:
            simple_comp = lambda z: z > (150 - x)
            simple_comp_2 = lambda z: z > (200 - x)
            params = [{'comparer': simple_comp, 'heuristic': brightness, 'num_rotations': 1},
                      {'comparer': simple_comp_2, 'heuristic': brightness, 'num_rotations': 2}]
            f_t = multisort(frame, params)
            out.write(f_t)

    cam.release()

    cv2.destroyAllWindows()
    out.release()
