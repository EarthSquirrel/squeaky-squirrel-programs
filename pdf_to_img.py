# import module
from pdf2image import convert_from_path

path = '/Users/britney/Documents/photo scans/texas 2009/001-087 after that messed up.pdf'
save_path = '/Users/britney/Documents/photo scans/texas 2009/'

# starting number of image
start = 1

# Store Pdf with convert_from_path function
images = convert_from_path(path)

for i in range(1, len(images), 2):
    num = str(start)
    if len(num) == 1:
        num = '00' + num
    else len(num) == 2:
        num = '0' + num
    # assume only goes to three digits

    # increment start
    start += 1

    # Save pages as images in the pdf
    images[i].save(save_path + num + '.jpg', 'JPEG')
