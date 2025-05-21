import cv2 as cv, numpy as np

print(cv.__version__, np.__version__)

video = cv.VideoCapture(0) # first camera video input enabled


def see_your_video():
    while True:

        ret, frame = video.read()

        cv.imshow("Camera", frame)

        if cv.waitKey(5) == ord("x"):
            break


def laplacian_video():
    while True:

        ret, frame = video.read()

        cv.imshow("Camera", frame)

        laplacian = cv.Laplacian(frame, cv.CV_64F)
        laplacian = np.uint8(laplacian)
        cv.imshow("laplacian", laplacian)

        edges = cv.Canny(frame, 100, 100)
        cv.imshow("Canny", edges)
        if cv.waitKey(5) == ord("x"):
            break


#see_your_video()
laplacian_video()

cv.destroyAllWindows()
video.release()
