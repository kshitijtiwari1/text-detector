import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


image = cv2.imread("/home/kshitij/Python Projects/text-detection/image1.png")

image_copy = image.copy()
target_word = "best"

data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

word_occurences = [ i for i, word in enumerate(data["text"]) if word == target_word ]

for occurence in word_occurences:
    # extract the width, height, top and left position for that detected word
    w = data["width"][occurence]
    h = data["height"][occurence]
    l = data["left"][occurence]
    t = data["top"][occurence]
    # define all the surrounding box points
    p1 = (l, t)
    p2 = (l + w, t)
    p3 = (l + w, t + h)
    p4 = (l, t + h)
    # draw the 4 lines (rectangular)
    image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)

plt.imsave("copy-of-image1.png", image_copy)
plt.imshow(image_copy)
plt.show()