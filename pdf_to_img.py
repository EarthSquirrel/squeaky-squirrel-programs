# import module
from pdf2image import convert_from_path

path = '/Users/britney/Documents/photo scans/texas 2009/001-087 after that messed up.pdf'
save_path = '/Users/britney/Documents/photo scans/texas 2009/'
# Store Pdf with convert_from_path function
images = convert_from_path(path)

for i in range(1, len(images), 2):
    num = str(i)
    # Save pages as images in the pdf

    images[i].save(save_path + num + '.jpg', 'JPEG')
