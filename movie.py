import cv2
from orst import sort
from orst import summation


if __name__ == "__main__":

    def simple_comp(x):
        return x > 200

    num_frames = 100
    cam = cv2.VideoCapture("path.mp4")

    ret, frame = cam.read()

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(
        "output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 20, frame.shape[:-1][::-1]
    )

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
