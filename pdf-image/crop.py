# Crop all images in a folder
# https://www.geeksforgeeks.org/python-pil-image-crop-method/
from PIL import Image 
import os

def crop_bottom(dir_path, cut_off):
    jpgs = []  # array for images that are jpgs
    for f in os.listdir(dir_path):
        if f.endswith('.jpg'):
            print(f)

    # Opens a image in RGB mode 
    im = Image.open("/Users/britney/Documents/photo scans/barb's flipbook 01/01.jpg") 

    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 

    # Setting the points for cropped image 
    left = 0
    top = 0
    right = width
    bottom = height - 125

    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 

    # Shows the image in image viewer 
    #im.show()
    #im1.show()
    #print(im1.size)


if __name__ == '__main__':
    # left, top, right, bottom
   crop_bottom("/Users/britney/Documents/photo scans/barb's flipbook 01", 125)
