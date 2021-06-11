from Dropbox import uplaodDropBox
import time
import cv2
import random
import dropbox

startTime = time.time()

def StorePic():
    rNumber = random.randint(0,100)
    accesCamera = cv2.VideoCapture(0)

    while (True):
        ret,frame = accesCamera.read()
        imageName = "ImageForDropBox" + str(rNumber) + ".png"
        cv2.imwrite(imageName,frame)
        global startTime 
        startTime = time.time()
        break

    accesCamera.release()
    cv2.destroyAllWindows()

    return imageName

def UploadToDropBox(imageName):
    accessToken = 'sl.AyghAmhb5zXA7yY_3fqdmouUhQpZgeByCL7CmaQuUfxsgQ4hBjgmjturQrdqHOCPpzyDuOpJsmdoRjmq_pz0HKBVtUkcUCrwyTMiAMxv2MAFnhE6xGu_8vM4wfgw6ALxZt-M2bQaEZs'
    fileFrom = imageName
    targetFile = "/folder1/" + imageName
    connection = dropbox.Dropbox(accessToken)

    with open(fileFrom,"rb") as f:
        connection.files_upload(f.read(), targetFile, mode = dropbox.files.WriteMode.overwrite)
        print("succussfully uploaded!!")

def main():
    while (True):
        if ((time.time() - startTime) >= 30):
            imageName = StorePic()
            UploadToDropBox(imageName)

main()




    

