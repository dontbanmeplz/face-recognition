from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory")
ap.add_argument("-i", "--input", required=True,
	help="path to input file")
args = vars(ap.parse_args())

os.chdir(args["output"])
# load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier(args["cascade"])
# initialize the video stream, allow the camera sensor to warm up,
# and initialize the total number of example faces written to disk
# thus far
print("[INFO] starting video stream...")
vs =  cv2.VideoCapture(args["input"])
# vs = VideoStream(usePiCamera=True).start()
t = 0
success = True




# loop over the frames from the video stream
while success:
	if t != 6:
		t += 1
		success, frame = vs.read()
		continue
	else:
		pass
	# grab the frame from the threaded video stream, clone it, (just
	# in case we want to write it to disk), and then resize the frame
	# so we can apply face detection faster
	success, frame = vs.read()
	orig = frame.copy()
	frame = imutils.resize(frame, width=400)
	# detect faces in the grayscale fram
    
	# show the output 
	# if the `k` key was pressed, write the *original* frame to disk
	# so we can later process it and use it for face recognition
	
	p = os.path.sep.join([args["output"], "{}.png".format(str(total).zfill(5))])
	cv2.imwrite(p, orig)
