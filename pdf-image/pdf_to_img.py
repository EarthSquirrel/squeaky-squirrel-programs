#  https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
from pdf2image import convert_from_path
import numpy as np
import sys



def two_name(num):
    # get the number of an image
    if len(num) == 1:
        num = '{}{}'.format('0', num)
    elif len(num) == 2:
        num = '{}{}'.format('', num)
    # assume only goes to three digits
    return num

def three_name(num):
    # get the number of an image
    if len(num) == 1:
        num = '{}{}'.format('00', num)
    elif len(num) == 2:
        num = '{}{}'.format('0', num)
    # assume only goes to three digits
    return num


def convert(start, digit, path, save_path, white_thresh=725, detect_white=True):
    # make sure save_path ends with /
    if not save_path.endswith('/'):
        save_path = save_path + '/'
    
    # Store Pdf with convert_from_path function
    images = convert_from_path(path, 600)
    print('Converting a {} page PDF to images'.format(len(images)))

    for i in range(0, len(images), 1):
        num = str(start)
        
        img = images[i]
        width, height = img.size
        avg = 0
        if detect_white:
            for w in range(width):
                for h in range(height):
                    avg += np.sum(img.getpixel((w, h)))
            
            avg = avg/(width*height)
            
            
            # get the number for the image
            if avg < white_thresh:
                num = start
                # increment start
                start += 1
            else:
                num = start - 1
        else: 
            start += 1  # comment out if using white detector
        
        # convert num to string
        num = str(num)
        # get the name with number of digits
        if digit == 1:
            pass
        elif digit == 2:
            num = two_name(num)
        elif digit == 3:
            num = three_name(num)
        else:
            print('Digit value must be either 1, 2, or 3')
            sys.exit()
        
        # add the back if necessary
        if avg >= 725:
            num = 'back-' + num

        # Save pages as images in the pdf
        images[i].save(save_path + num + '.jpg', 'JPEG')


if __name__ == '__main__':
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
    white_thresh = 725

    convert(start, digit, path, save_path, white_thresh) 
    

