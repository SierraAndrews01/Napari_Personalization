from PIL.Image import Image
from skimage import data
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

def create_photo_array(image_stack, viewer):
    photo_arrays = list() * 153
    counter = 0

    print("Before for statement")
    for file in os.listdir(image_stack):
        # Read filename
        filename = os.fsdecode(file)

        # Split the name into the name and extension
        split_tup = os.path.splitext(filename)
        print(split_tup)

        # Create file extension variable
        file_extension = split_tup[1]

        # Creates the list that the images (as arrays) are stored in

        # If the extension is not a TIFF file it ignores it and prints/increments the counter
        # if file_extension != ".tif":
        if counter <= 6:
            print(counter)
            counter = counter + 1
        # If it is a TIFF file it creates a path for it, reads the image, and converts
        # it to a numpy array that is then added to a list
        else:
            # Creates file directory
            tif_path = image_stack + '\\' + filename
            image = tifffile.imread(tif_path)

            # Convert the image to a NumPy array
            image_array = np.array(image)

            # Stores photo array in list
            photo_arrays.append(image_array)

            # increments counter
            counter = counter + 1

    # converts list to array ?
    nparry = np.array(photo_arrays)
    print("After nparry is created")
    print(image_stack[1])
    new_layer = viewer.add_image(nparry)
    new_layer.colormap = 'green'
    napari.view_image(data=nparry, ndisplay=3)
    napari.run()
    return nparry

def main():
    practice_image = 'C:\\Users\\andrewss\\PycharmProjects\\pythonProject\\JW_R03_nerve_stack\\JW_R_030000_2022-09-13T11-11-45.333.tif'
    directory = 'C:\\Users\\andrewss\\PycharmProjects\\pythonProject\\JW_R03_nerve_stack'
    viewer = napari.Viewer(ndisplay=3)
    numpy_array = create_photo_array(directory, viewer)
    print()
    print("After numpy_array is created")
    #line_mapping(practice_image)
    print("After line mapping")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()