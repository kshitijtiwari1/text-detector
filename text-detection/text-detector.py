import pytesseract
import cv2
import matplotlib.pyplot as plt
import sys
from PIL import Image

image = cv2.imread("/home/kshitij/Python Projects/text-detection/image1.png")

string = pytesseract.image_to_string(image)
print(string)

data = pytesseract.image_to_data(image)

print(data)