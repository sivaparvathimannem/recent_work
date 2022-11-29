# Read video
import cv2
import sys 

video = cv2.VideoCapture("/home/ailand/depthai-python/video.mp4")
#video = cv2.VideoCapture(0) # for using CAM

# Exit if video not opened.
if not video.isOpened():
  print("Could not open video")
  sys.exit()

# Read first frame.
ok, frame = video.read()
if not ok:
  print ('Cannot read video file')
  sys.exit()