'''
    @FileName:Test.py
    @Author:yikai yang
    @Date:2023/5/27
    @Desc:Null
'''
import cv2

from Functions.DetectVideo import DetectVideo
from Functions.DrawHeat import DrawHeat

path = "C:\\Users\\yangyikai\\Desktop\\Graduate\\Test\\test2.mp4"
# Load the image
video = cv2.VideoCapture(path)
x, y, width, height = 467, 495, 55, 98
roi = (int(x), int(y), int(width), int(height))
ret, frame = video.read()

x, y, width, height = roi
roi_frame = frame[y:y + height, x:x + width]

cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
# Convert the image to grayscale

cv2.imwrite("thresholded.jpg", frame)


