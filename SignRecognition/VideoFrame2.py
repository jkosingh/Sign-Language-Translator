from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import cv
import os
import keyboard
import glob
import numpy as np
from skimage.measure import compare_ssim as ssim
import skimage.transform
import matplotlib.pyplot as plt
import scipy

dir = "/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/TEST_VIDS/big_buck_bunny_720p_5mb.mp4"


vidcap = cv2.VideoCapture(dir)
success,image = vidcap.read()
count = 0  # initialize counter
while success:
  vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC,(count*5000))    # Change multiple on count for number of frames taken  
  cv2.imwrite("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/EXPORT/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success, ' ', count)
  count += 1
  comp = False

if success == False:
  print('DONE SPLICING VIDEO INTO FRAMES')
  Y_data = [] # Frames from video
  export = glob.glob("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/EXPORT/*.jpg")
  for pegs in export:
    frames = cv2.imread(pegs)
    Y_data.append(frames) #array to hold exported pictures
  print('Frames to compare array size', len(Y_data))
  X_data = [] # Database sign langauge pictures
  database = glob.glob ("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/DATABASE/*.jpg")
  for myFile in database:
    image = cv2.imread (myFile)
    X_data.append (image)
  print('Database Array size:', len(X_data))
  print('DONE CREATING ARRAYS TO COMPARE')
  comp = True
else:
  print('I Suck')
  comp = False

if comp == True:
  print('NOW WILL COMPARE ARRAYS')
  tolerance = 0.9
  counted = 0
  deleted =0
  for i in range(0,len(Y_data)):
     for j in range(0,len(X_data)):
       Databased = cv2.cvtColor(X_data[j], cv2.COLOR_BGR2GRAY)
       Exported = cv2.cvtColor(Y_data[i], cv2.COLOR_BGR2GRAY)
       Databased = skimage.transform.resize(Databased, Exported.shape, mode='constant')
       s = ssim(Exported, Databased)
       WantToDelete = True
       if s > tolerance:
	 counted+=1
         print("Files still in folder: ", counted)
	 WantToDelete = False
     if WantToDelete:    
     	#delete picture from database
	print("{}".format(export[i]))	
	os.remove("{}".format(export[i]))	
     	deleted+=1
     	#print("Files deleted: ", deleted)
  #print Databased.shape
  #print Exported.shape
  #s = ssim(original, original)
  #print("MSE: ", m)
  #print ("SSIM: ", s)
else:
  print('I still suck')
