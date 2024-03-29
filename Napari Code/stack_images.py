from __future__ import print_function
from PIL.Image import Image
from skimage import data, io
import napari
import os
import numpy as np
import PyQt5
import PIL
from PIL import Image
import h5py
import tifffile
import imagecodecs
#import napari-deeplabcut
import deeplabcut
# import cv2 as cv
import numpy as np
import argparse
import os
from types import NoneType
import napari
import cv2 as cv
import numpy as np
import argparse
from pathlib import Path
import tifffile

def create_empty_tif(directory, filename):
    print("Current directory:", os.getcwd())
    # Define numpy array shape
    shape = (512, 512, 3)
    # Check if stack folder exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Check if the file exists
    if os.path.exists(filename):
        # If it exists, delete the file
        os.remove(filename)
        print(f"Existing file '{filename}' deleted.")

    # Create an empty array of the specified shape
    empty_array = np.zeros(shape)

    # Save the empty array as a TIFF file
    tifffile.imwrite(filename, empty_array)
    print(f"New empty TIFF file created: '{filename}'")



# assign directory to read images from
directory = "C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\Mapped_Images"

# assign directory that stack will be stored in
final_stack = directory + "\\Stack\\final_stack.tif"

# Create empty tiff file to store the image stack in
create_empty_tif(directory + "\\Stack", final_stack)

# iterate over files in
# that directory
for filename in os.listdir(directory):
    if(filename == "adapted_JW_R_030152.tif" or filename == "Stack"):
        print("Last file")
    else:
        # reads whole path (with file in it)
        f = os.path.join(directory, filename)
        # Creates the image object from said path
        print(f)
        print("Before image creation")
        temp_image = tifffile.imread(f)
        print(filename)
        # Transforms image into numpy array
        temp_f_np = np.array(temp_image)
        # Prints shape for tester
        print(temp_f_np.shape)
        # Writes image (temp_f_np) to specified path (final_stack)
        tifffile.imwrite(final_stack, temp_f_np)

final_image = tifffile.imread(final_stack)
final_image_np = np.array(final_image)
shape = final_image_np.shape
print(shape)
print("Reached the end of the code")