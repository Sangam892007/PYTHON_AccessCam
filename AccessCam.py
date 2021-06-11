import cv2

def CameraPic():
    accessCamera = cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = accessCamera.read()

        cv2.imwrite("Frame1.jpg",frame)
        result = False
    
    accessCamera.release()
    cv2.destroyAllWindows()

CameraPic()
