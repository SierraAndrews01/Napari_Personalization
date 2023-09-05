from __future__ import print_function
import os
from types import NoneType

import cv2 as cv
import numpy as np
import argparse
import tifffile

from pathlib import Path

def main():
    # Create new folder or clear old folder
    analyzed_image_directory = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\Mapped_Images\\'
    directory_set_up(analyzed_image_directory)
    working_directory = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack'
    filenames = os.listdir(working_directory)
    counter = 0
    coordinate_list = list()

    for file in os.listdir(working_directory):
        if counter >= 32:
            full_image_path = working_directory + '\\' + filenames[counter]
            print(full_image_path)
            src = cv.imread(full_image_path)
            kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
            print(type(kernel))
            if file is None:
                print('Could not open or find the image: ', file)
                exit(0)
            # Erodes and dilates
            opened_image = cv.morphologyEx(src, cv.MORPH_OPEN, kernel)
            lines = plot_lines(analyzed_image_directory, opened_image, filenames[counter])
            coordinate_list.append(lines)
            cv.waitKey(0)
            cv.destroyAllWindows()
        counter = counter + 1

        #lines = plot_lines(opened_image)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
#  [main]


# If we cant get napari points, we can save the copy of
# the image with the lines over it and display that copy
def plot_lines(directory, image, image_name):
    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Use canny edge detection
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    # apply binary thresholding
    ret, thresh = cv.threshold(edges, 150, 255, cv.THRESH_BINARY)
    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    # draw contours
    image_copy = image.copy()
    cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                    lineType=cv.LINE_AA)

    store_new_image(directory, image_name, image_copy)
    return contours

'''
    # Apply HoughLinesP method to
    # directly obtain line end points
    lines_list = []
    lines = cv.HoughLinesP(
        edges,  # Input edge image
        0.5,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        # 20 is probably a decent middle ground
        threshold=10,  # Min number of votes for valid line
        minLineLength=5,  # Min allowed length of line
        maxLineGap=45  # Max allowed gap between line for joining them
    )

    counter = 0
    # Iterate over points
    if type(lines) is NoneType:
        print("The variable is of NoneType")
        store_new_image(directory, image_name, image)
    else:
        for points in lines:
            # Extracted points nested in the list
            x1, y1, x2, y2 = points[0]
            # Draw the lines joining the points
            # On the original image
            cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Maintain a simples lookup list for points
            lines_list.append([(x1, y1), (x2, y2)])

        # Save the result image
        #cv.imshow(image_name, image)

        # Run save image method
        store_new_image(directory, image_name, image)

    return lines
    '''


def directory_set_up(path):
    if(os.path.exists(path)):
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
    else:
        # create new directory for new images
        os.makedirs(path)


def store_new_image(directory, image_name, image):
    cv.imwrite(directory + 'analyzed_' + image_name, image)


def create_photo_array(image_stack):
    photo_arrays = list() * 153
    counter = 0

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
            #print(counter)
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
    return photo_arrays

def find_filename(file):
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()