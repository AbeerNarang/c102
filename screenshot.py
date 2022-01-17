import cv2
def clickpicauto():
    videocaptureobject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        cv2.imwrite("photo1.png", frame)
        result = False
    videocaptureobject.release()    
    cv2.destroyAllWindows()
clickpicauto()