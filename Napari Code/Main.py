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
import cv2 as cv
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

        # Create file extension variable
        file_extension = split_tup[1]

        # Creates the list that the images (as arrays) are stored in

        # If the extension is not a TIFF file it ignores it and prints/increments the counter
        # if file_extension != ".tif":
        #   print("Fraud")
        #   print(counter)
        #    counter = counter + 1
        if counter <= 6:
            print(counter)
            counter = counter + 1
        # If the file doesn't have an extension it ignores it and prints/increments the counter
        # elif file_extension == "":
        # counter = counter + 1
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

            counter = counter + 1
    nparry = np.array(photo_arrays)
    new_layer = viewer.add_image(nparry)
    new_layer.colormap = 'green'
    napari.view_image(data=nparry, ndisplay=3)
    napari.run()

def plot_lines(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Use canny edge detection
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    # Apply HoughLinesP method to
    # directly obtain line end points
    lines_list = []
    lines = cv.HoughLinesP(
        edges,  # Input edge image
        0.5,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        threshold=40,  # Min number of votes for valid line
        minLineLength=5,  # Min allowed length of line
        maxLineGap=25  # Max allowed gap between line for joining them
    )

    # Iterate over points
    for points in lines:
        # Extracted points nested in the list
        x1, y1, x2, y2 = points[0]
        # Draw the lines joing the points
        # On the original image
        cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Maintain a simples lookup list for points
        lines_list.append([(x1, y1), (x2, y2)])

    # Save the result image
    cv.imshow('detectedLines.png', image)
    #return lines

def line_mapping(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    if image is None:
        print('Could not open or find the image: ', image)
        exit(0)
    opened_image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    cv.imshow('Original Image', image)
    cv.imshow('Opened Image', opened_image)
    lines = plot_lines(opened_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():
    directory = 'C:\\Users\\andrewss\\PycharmProjects\\pythonProject\\JW_R03_nerve_stack'
    viewer = napari.Viewer(ndisplay=3)
    numpy_array = create_photo_array(directory, viewer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()