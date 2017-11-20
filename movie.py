import cv2
import numpy as np
from orst import sort
from orst import brightness, summation


if __name__ == "__main__":

    simple_comp = lambda x: x > 200

    num_frames = 100
    cam = cv2.VideoCapture("koek_en_ei.mp4")

    ret, frame = cam.read()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 20, frame.shape[:-1][::-1])

    resultant_frames = []

    for x in range(num_frames):

        print(x)

        ret, frame = cam.read()
        if ret:
            f_t = sort(frame, simple_comp, summation)
            out.write(f_t)

    cam.release()

    cv2.destroyAllWindows()
    out.release()
