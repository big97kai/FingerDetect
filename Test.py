'''
    @FileName:Test.py
    @Author:yikai yang
    @Date:2023/5/27
    @Desc:Null
'''
import cv2

from Functions.DetectVideo import DetectVideo
from Functions.DrawHeat import DrawHeat

path = 'heat.jpg'
# Load the image
image = cv2.imread(path)  # Replace 'your_image_path.jpg' with the actual path to your image

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite("thresholded.jpg", thresholded)
# Get the pixel values of the gray image
pixel_values = gray_image.flatten()

# Print the pixel values
print(pixel_values)
