#  https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
from pdf2image import convert_from_path

path = '/Users/britney/Documents/photo scans/texas 2009/_02.pdf'
save_path = '/Users/britney/Documents/photo scans/texas 2009/'

# starting number of image
start = 44

# Store Pdf with convert_from_path function
images = convert_from_path(path)

for i in range(0, len(images), 2):
    num = str(start)
    if len(num) == 1:
        num = '{}{}'.format('00', num)
    elif len(num) == 2:
        num = '{}{}'.format('0', num)
    # assume only goes to three digits

    # increment start
    start += 1

    # Save pages as images in the pdf
    images[i].save(save_path + num + '.jpg', 'JPEG')
