import cv2 as cv


print(cv.__version__)
#video = cv.VideoCapture(0) # first camera video input enabled
video = cv.VideoCapture("ich.mp4")
subtractor = cv.createBackgroundSubtractorMOG2(100, 50)

while True:

    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord("x"):
            break

    else:
        video = cv.VideoCapture("ich.mp4")

cv.destroyAllWindows()
video.release()