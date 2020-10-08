import cv2
from orst import multisort
from orst import brightness


if __name__ == "__main__":

    num_frames = 150
    cam = cv2.VideoCapture(0)
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

            def simple_comp(x):
                return x > (150 - x)

            def simple_comp_2(x):
                return x > (200 - x)

            params = [
                {"comparer": simple_comp, "heuristic": brightness, "num_rotations": 1},
                {
                    "comparer": simple_comp_2,
                    "heuristic": brightness,
                    "num_rotations": 2,
                },
            ]
            f_t = multisort(frame, params)
            out.write(f_t)

    cam.release()

    cv2.destroyAllWindows()
    out.release()
