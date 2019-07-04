#!/usr/bin/env python2
"""This script resizes an image (various formats supported) to a fixed square size of 200x200:
BMP
EPS
GIF
ICNS
ICO
IM
JPEG
JPEG 2000
MSP
PCX
PNG
PPM
SGI
SPIDER
TIFF
WebP
XBM
"""
#CS-GY-9163
#SUMMER 2019

#Libraries
import os
import sys
import argparse
from PIL import Image

#function to open image and resize
def sq_resizer(path_to_file):
    """Resizes the image to a 200x200
    Args:
        path to file
    Returns:
        saves file in the same directory as argument
    Raises:
        IOError: when a file could not be opened or resized
        ValueError: when a file could not be saved
    """
    #opening image to resize
    try:
        image = Image.open(path_to_file)
        print "Resizing image now, please wait ..."
        try:
            image = image.resize((200, 200))
        except IOError, error_message:
            print error_message
            sys.exit(1)
    except IOError, error_message:
        print error_message
        sys.exit(1)
    #parsing input path to create new name for new resized image
    filename, extension = os.path.splitext(path_to_file)
    new_name = filename + "_square" + extension
    #same newly resized image with new name
    try:
        image.save(new_name)
        print "..."
        print "Done. Your new image has been saved as " + new_name
    except ValueError, error_message:
        print error_message
        sys.exit(1)
    except IOError, error_message:
        print error_message
        sys.exit(1)

def main(path_to_file):
    """Standard main function to call the resizer function"""
    sq_resizer(path_to_file)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(add_help=False)
    PARSER.add_argument("path_to_file", help="path to file to be resized here")
    PARSER.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Fully supported format: \
    BMP \
    EPS \
    GIF \
    ICNS \
    ICO \
    IM \
    JPEG \
    JPEG 2000 \
    MSP \
    PCX \
    PNG \
    PPM \
    SGI \
    SPIDER \
    TIFF \
    WebP \
    XBM')
    ARGS = PARSER.parse_args()
    main(ARGS.path_to_file)
