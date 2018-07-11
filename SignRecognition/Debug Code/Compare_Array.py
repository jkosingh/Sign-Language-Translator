import cv2
import glob
import numpy as np

X_data = []
files = glob.glob ("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/DATABASE/*.jpg")
for myFile in files:
    print(myFile)
    image = cv2.imread (myFile)
    X_data.append (image)

print('X_data size:', len(X_data))
