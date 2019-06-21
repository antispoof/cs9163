#!/usr/bin/env python2

#CS-GY-9163
#SUMMER 2019

#modules needed
import os, sys
import argparse
from PIL import Image

#function to open image and resize
def sq_resizer(path_to_file):
	#opening image to resize
	try:
		image = Image.open(path_to_file)
			
		print "Resizing image now, please wait ..."
		try:
			image = image.resize((200, 200))
		except IOError, e:
			print e
			sys.exit(1)
	except IOError, e:
		print e
		sys.exit(1)
	#parsing input path to create new name for new resized image
	filename, extension = os.path.splitext(path_to_file)
	new_name = filename + "_square.jpg"
	#same newly resized image with new name
	try:
		image.save(new_name)
		print "..."
		print "Done. Your new image has been saved as " + new_name 
	except ValueError, e:
		print e
		sys.exit(1)

def main(path_to_file):
	sq_resizer(path_to_file)

if __name__ == "__main__": 
	parser = argparse.ArgumentParser()
	parser.add_argument("path_to_file", help="file to be resized here")
	args = parser.parse_args()
	main(args.path_to_file) 
