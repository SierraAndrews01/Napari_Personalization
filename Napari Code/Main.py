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
import tifffile
from pathlib import Path

def main():
    # Load images as a stack when Napari opens
    print("Beginning of main method")

    # path to 3d stack
    threeD_stack = "C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\output_test.tif"

    # Create a simple 3D array
    numpy_data = cv.imread(threeD_stack)

    print(numpy_data.shape)

    image_stack_path = "C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\Mapped_Images\\Mapped_Stack\\mapped_im_stack.tif"

    # image = tifffile.imread(threeD_stack)
    image = tifffile.imread(image_stack_path)
    viewer = napari.view_image(image, rgb=True)


    # Run the Napari GUI
    napari.run()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()
