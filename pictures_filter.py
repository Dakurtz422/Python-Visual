import glob
import cv2
import os

dir = "Downloads/*.png"
counter = 0
target_height = 224
target_width = 224

class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

    def shape(self):
        self.height, self.width, self.channels = self.img.shape
        return self.height, self.width, self.channels


images = [MyImage(file) for file in glob.glob(dir)]
for image in images:
    height, width, _ = image.shape()
    if int(height) < target_height or int(width) < target_width:
        print(f"{str(image)} - DELETED")
        os.remove(str(image))
        counter +=1
    else:
        print(f"{str(image)} - PASS")

print(f"{counter} Pictures deleted")
