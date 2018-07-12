from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import cv
import os
import keyboard
import glob
import numpy as np

#dir = "/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/TEST_VIDS/big_buck_bunny_720p_5mb.mp4"
dir = "/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/TEST_VIDS/Learn ASL Alphabet Video.mp4"
vidcap = cv2.VideoCapture(dir)
success,image = vidcap.read()
count = 0  # initialize counter
while success and 1:
  vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC,(count*1000))    # Change multiple on count for number of frames taken  
  cv2.imwrite("/home/jsingh/Codeblocks Projects/PROJECT/SignRecognition/DATA/EXPORT/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
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
else:
  print('I still suck')
