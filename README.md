# Sign-Language-Translator
Be able to acknowledge sign language graphically. Multiple uses. 

	TO RUN CODE RIGHT NOW
Run Code by running:  python VideoFrame2.py
	Need to run from SignRecognition directory. This will create frames and extract to SignRecognition/DATA/EXPORT directory and 		then port them into an array (Y_data). Then in will do the same for the pictures in SignRecognition/DATA/DATABASE directory 		porting them into another array (X_data). No comparison algorithm running yet, but will implement a sci-images one in a double 		for loop for next patch. 
	** Also can run: python Empty_Output_Directory.py
	to empty out the SignRecognition/DATA/EXPORT after every run.
 	***Also need to change directory paths to match your configuration in all python files run. 

	Description of the Project
The idea behind this project is to successfully capture a sequence of American Sign Language symbols via camera and, through image processing, translate the hand gestures into English text.


	Objectives of Project 
Be able to successfully recognize American Sign Language through live video and translate successfully into text through the following steps:
	Render video footage (of average phone camera quality) into frames using python and openGL scripting to compare with sign 		language database
	Segment the area of interest from the frames using image processing techniques in python, specifically the scikit library to 		achieve imaging labeling
	Implement multiple feature extraction algorithms to represent image data in a more useful way
	Train algorithm to recognize the data using multiple machine learning algorithms or database lookup for pattern recognition, 		classification and regression to match proper sign language symbols
	Translate recognized sign language symbols to text through use of lookup table or machine learning algorithm and display for 		user


	Expected Methodologies
	
   		K Nearest Neighbors Algorithm
Algorithm in pattern recognition for classification and regression. For specified odd value of K, the image is partitioned into groups to determine which part is hand and which is background. Support and documentation on how to achieve this using OpenCV, python and scilabs found here [28]: https://docs.opencv.org/2.4/modules/ml/doc/k_nearest_neighbors.html 
        
    Logistic Regression
Borrowed from statistics for classification similar to linear regression to help us tell what is part of the hand to what is background. Specifically the logistic function maps any input value taken in (image vector representation) and maps it into a binary value of  0 or 1. This is done with the formula:
y = e^(b0 + b1*x) / (1 + e^(b0 + b1*x))
Where x is your input and b0 and b1 are weights calculated from probabilities and predictions made on the data. Support and documentation on how to achieve this using OpenCV, python and scilabs found here [29]: https://machinelearningmastery.com/logistic-regression-for-machine-learning/ 


     Support Vector Machine 
A supervised machine learning algorithm, meaning given a input variable and a output variable, the algorithm will try to find the mapping function of x and y. The end goal of using this algorithm is to teach the program enough, that it will be able to take in new input data and predict the output independently to an acceptable extent. SVM particularly, uses a technique called the kernel trick which transforms the input vector representation data through extremely complex transformations to find the optimal boundary between possible outputs based on the labels already previously defined.  Support and documentation on how this is done in python using scilabs can be found here [30]: https://www.kdnuggets.com/2017/02/yhat-support-vector-machine.html 


     Naive Bayes
Yet another classification technique, this time giving us the best assumption fit. The bayes algorithm creates a hypothesis based on prior knowledge (training) and produces a probability of what the output should be. Advantages of this algorithm are that it is simple and fast and requires less training time, but is suggested to be best used when trying to identify text. Support and documentation on how this is done in python using scilabs can be found here [31]: http://scikit-learn.org/stable/modules/naive_bayes.html 


     Random Forest
Another classification techniques, very similar to the previous Naive Bayes algorithm. The Random forest algorithm is a supervised learning algorithm based on the idea that using a lot of different combinational learning models increase the overall accuracy of the result. The biggest advantage of it is that it can be used for not only classification, but also regression in machine learning. Support and documentation on how this is done in python can be found here [32]: https://towardsdatascience.com/the-random-forest-algorithm-d457d499ffcd
  
  
     Histogram of Oriented Gradients
The Histogram of Oriented Gradients method of representing image pixels in vector form for input into later machine learning algorithms. The algorithm can be used for our project to take the frames collected from the video of the sign language happening and transfer it into a more useful representation. For more information on implementation in python and use [33]: https://jakevdp.github.io/PythonDataScienceHandbook/05.14-image-features.html 

	OpenCV Image Processing
To Segment the area of interest from the frames, we must using image processing techniques in python or openCV. Although there are many implementations out there, for sake of code completion and integration, we’ll try to achieve this using the the scikit-image library. For a list of implementations that could be done in python as well as there documentation please visit [34]: http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_label.html 
