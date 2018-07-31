import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob
import os
from skimage.measure import compare_ssim as ssim
from skimage.transform import resize
from skimage.transform import rescale
from PIL import Image
import skimage.transform
from skimage import io, color
from scipy.ndimage import imread
#https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
dir = "\Users\justi\Downloads\Sign-Language-Translator-master\SignRecognition\TEST_VIDS\Learn ASL Alphabet Video.mp4"
vidcap = cv2.VideoCapture(dir)
vidcap.set(cv2.CAP_PROP_FRAME_WIDTH, 330)
vidcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 440)
success,image = vidcap.read()
count = 0  # initialize counter
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # Change multiple on count for number of frames taken
  cv2.imwrite("\Users\justi\Downloads\Sign-Language-Translator-master\SignRecognition\DATA\EXPORT\ frame%d.jpg" % count,image)  # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success, ' ', count)
  count += 1
  if count > 100: #Here because idk why ASL video never ends...
    success = False
  comp = False

if success == False:

  print('DONE SPLICING VIDEO INTO FRAMES')
  Y_data = [] # Frames from video
  export = glob.glob("\Users\justi\Downloads\Sign-Language-Translator-master\SignRecognition\DATA\EXPORT\*.jpg")
  for pegs in export:
    frames = cv2.imread(pegs)
    Y_data.append(frames) #array to hold exported pictures
    

  X_data = []  # Database sign langauge pictures
  database = glob.glob("\Users\justi\Downloads\Sign-Language-Translator-master\SignRecognition\DATA\DATABASE\*.jpg")
  #database = glob.glob("\Users\justi\Downloads\Sign-Language-Translator-master\SignRecognition\DATA\extractor\*.png")
  for myFile in database:
    image = cv2.imread(myFile)
    X_data.append(image)
    
print('Frames to compare array size', len(Y_data))
print('Database Array size:', len(X_data))
print('DONE CREATING ARRAYS TO COMPARE')

def resize_image_aspect_ratio(image, new_width=None, new_height=None):
    height, width = image.shape[:2]
    if new_width is not None and new_height is None:
        r = new_width/width
        new_height = int(height*r)
    elif new_width is None and new_height is not None:
        r = new_height/height
        new_width = int(width*r)
    new_image = cv2.resize(image, (new_height, new_width))
    #print("New Image Shape: ", new_image.shape)
    return new_image

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, pic1, pic2, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB, multichannel=True)
    if(m < 6000 and s> 0.9):
        # setup the figure

        print("found a match !!!!!!!!!!")
        print("Files checked: SSIM Value: ", s, "MSE Value: ", m, "FRAME: ", pic1, "Database", pic2)

        fig = plt.figure(title)
        plt.suptitle("MSE: %.2f, SSIM: %.10f" % (m, s))

        # show first image
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(imageA, cmap=plt.cm.gray)
        plt.axis("off")

        # show the second image
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(imageB, cmap=plt.cm.gray)
        plt.axis("off")

        # show the images
        plt.show()
    else:
        print("Not a match", "SSIM Value: ", s, " MSE Value: ", m)

for i in range(0, len(Y_data)):
        WantToDelete = True
        for j in range(0, len(X_data)):
            dbase = cv2.cvtColor(X_data[j], cv2.COLOR_BGR2GRAY)
            rames = cv2.cvtColor(Y_data[i], cv2.COLOR_BGR2GRAY)
            rames = rames[150:550,200:1100]
            #dbase = dbase[150:550,200:1100]
            #rames = resize(rames, dbase.shape, mode='constant')
            wi, he = dbase.shape
            #print("Shape: ", dbase.shape, " Width: ", wi, " Height", he)

            #resize_image_aspect_ratio(rames,wi,he)
            #print(" Frame Shape: ", rames.shape)


            #rames = resize(rames, dbase.shape, preserve_range=True)
            compare_images(resize_image_aspect_ratio(rames,wi,he), dbase, export[i], database[j], "FRAMES vs. Database")

