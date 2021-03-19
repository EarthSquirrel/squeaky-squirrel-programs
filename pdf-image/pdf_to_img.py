#  https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
from pdf2image import convert_from_path
import numpy as np
import sys

# read in parameters from terminal
if len(sys.argv) < 5:
    print('Must add comand line argunments')
    print('Starting number, digits in name, original pdf, final folder path')
    print('Digits 1-4, where 1 is x.jpg, 2 is xx.jpg and so on')
    sys.exit()

start = int(sys.argv[1])
digit = int(sys.argv[2])
path = sys.argv[3]
save_path = sys.argv[4]


#path = '/Users/britney/Documents/photo scans/texas 2009/_02.pdf'
#save_path = '/Users/britney/Documents/photo scans/texas 2009/'

# starting number of image
#start = 44

# Store Pdf with convert_from_path function
images = convert_from_path(path)
print('Converting a {} page PDF to images'.format(len(images)))

for i in range(0, len(images), 1):
    num = str(start)
    
    img = images[i]
    width, height = img.size
    avg = 0
    for w in range(width):
        for h in range(height):
            avg += np.sum(img.getpixel((w, h)))
    
    avg = avg/(width*height)
    print(avg)
    

    if len(num) == 1:
        num = '{}{}'.format('0', num)
    elif len(num) == 2:
        num = '{}{}'.format('', num)
    # assume only goes to three digits

    # increment start
    start += 1
    

    # Save pages as images in the pdf
    images[i].save(save_path + num + '.jpg', 'JPEG')
