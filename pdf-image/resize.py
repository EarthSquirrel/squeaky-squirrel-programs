import os
import sys
from datetime import datetime as dt
from PIL import Image
import numpy as np


def resize4x6(path):
    # get all files in directory
    imgs = os.listdir(path)

    # remove pictures starting with _
    imgs = [x for x in imgs if not x.startswith('_') and not x.startswith('.')
            and os.path.isfile(os.path.join(path,x))]

    # create folder to move old ones to
    folder_name = 'old_' + str(dt.now())
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # for each image
    for img_name in imgs:
        #print(img_name)
        img_path = os.path.join(path, img_name)

        # read in image size
        img = Image.open(img_path)
        width, height = img.size

        # pick if should resize to 6 or 4 side
        new_dims = []
        if height > width:

            img = img.rotate(90, expand=True)
            width, height = img.size
        # do 4 first then go for 6
        # testing 4in (386 px)
        # 600 dpi
        in4 = 2400 #386
        in6 = 3600 #576
        x = int(width*in4/height)
        if x <= in6:
            new_dims = [x, in4]

        # testing 6in (576 px)
        x = int(height*in6/width)
        if x <= in4:
            new_dims = [in6, x]

        # resize the image
        img = img.resize(new_dims)
        #img.show()

        # fill in rest with white space
        # make a white image
        white = Image.new('RGB', (in6, in4), (255, 255, 255))

        # fill in pixels of image that fit
        white.paste(img, (0,0))
        #white.show()
        # tada!
        new_img_name = '4x6_' + img_name
        white.save(os.path.join(path, new_img_name), dpi=(600,600), quality=95)
        new_img_path = os.path.join(path, folder_name, img_name)
        os.rename(img_path, new_img_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Add a path to evaluate images at')
        sys.exit()

    path = sys.argv[1]
    resize4x6(path)
