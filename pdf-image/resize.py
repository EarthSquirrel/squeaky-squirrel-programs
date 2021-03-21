import os
import sys

def resize4x6(path):
    # get all files in directory
    pics = os.listdir(path)

    # remove pictures starting with _
    pics = [x for x in pics if not x.startswith('_')]
    print(pics)

    # create folder to move old ones to

    # pick if should resize to 6 or 4 side

    # fill in rest with white space


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Add a path to evaluate images at')
        sys.exit()

    path = sys.argv[1]
    resize4x6(path)
