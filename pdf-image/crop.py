# Crop all images in a folder
# https://www.geeksforgeeks.org/python-pil-image-crop-method/
from PIL import Image
import os

def crop(dir_path, crop_off):
    # make folder for croped images
    cropped_path = os.path.join(dir_path, 'cropped')
    if not os.path.exists(cropped_path):
        os.mkdir(cropped_path)


    jpgs = []  # array for images that are jpgs
    for f in os.listdir(dir_path):
        # only take images
        if f.endswith('.jpg'):
            path = os.path.join(dir_path, f)
            jpgs.append([path, f])

    for img_path,f in jpgs:
        # Opens a image in RGB mode
        im = Image.open(img_path)

        # Size of the image in pixels (size of orginal image)
        # (This is not mandatory)
        width, height = im.size

        # Setting the points for cropped image
        left = 0 + crop_off[0]
        top = 0 + crop_off[1]
        right = width - crop_off[2]
        bottom = height - crop_off[3]

        # Cropped image of above dimension
        # (It will not change orginal image)
        cropped_img = im.crop((left, top, right, bottom))

        # save the image
        save_path = os.path.join(cropped_path, f)
        cropped_img.save(save_path)

        # Shows the image in image viewer
        #im.show()
        #im1.show()
        #print(im1.size)


if __name__ == '__main__':
    # left, top, right, bottom
    '''
    crop_off = [0, 0, 0, 125]
    folders =  ['01', '02', '03', '04', '05', '06 - duplicate 05', '07', '08',
                '09', '10', '11', '12']
    for fol in folders:
        path = "/Users/britney/Documents/photo scans/barb's flipbook {}".format(fol)
        crop(path, crop_off)
    '''

    '''
    # 13 Ohio Sept 95
    # left, top, right, bottom
    crop_off = [0, 0, 100, 0]
    path = "/Users/britney/Documents/photo scans/barb's flipbook 13 Ohio Sept 95"
    crop(path, crop_off)
    '''

    crop_off = [0, 0, 0, 125]
    path = "/Users/britney/Desktop/Barb/barb's flipbooks"
    crop(path, crop_off)
