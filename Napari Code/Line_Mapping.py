from __future__ import print_function
import os
from types import NoneType

import napari
import cv2 as cv
import numpy as np
import argparse
import tifffile
from PIL import Image
from PIL import TiffImagePlugin

from pathlib import Path

"""
This class maps the images
The goal is for this class to take an array of images, analyze each individual image 
(with lines mapped over the original image), and return an array of the new mapped images
"""

"""
This main method selects 7 practice images and calls the image_testing method
"""
def main():
    print("Beginning of main method")

    # Create an array that stores the path and filename of each file
    # OR Create a dictionary with the name as the key and the path as the value
    # Use a for loop to loop through every file in the directory
    # Check if file is empty
    # If it's not:
    # Call image_testing?

    # Create dictionary to store all [file_name, morphed_image]
    morphed_image_set = {}
    # Create list to store just mapped images
    mapped_im_list = []
    # Create a variable that holds the path that contains the images
    test_directory = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack'
    # Create a list of all files in a directory
    files = os.listdir(test_directory)
    # Calculate number of files in test directory
    num_files = dir_size(test_directory)
    # File output directory path
    output_dir = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\Mapped_Images'
    for i in range(num_files):
        # A statement put in to remove any wrong file types or sizes
        if i < 10:
            print(i)
        else:
            # call and store the result from the find filename method
            temp_filename = find_filename(files[i])
            # call and store the results from the find file path method
            temp_filepath = find_filepath(files[i])

            # morph image
            #adapted_image = image_testing(temp_filepath, temp_filename + "_adapted")
            temp_image = cv.imread(temp_filepath, cv.IMREAD_COLOR)

            temp_morphed_image = plot_lines(temp_image)
            # Add the filename (as key) and image (as value) to dictionary (for storage purposes)
            morphed_image_set[i - 10] = ['adapted_' + temp_filename, temp_morphed_image]

    print(len(morphed_image_set))
    dir_path = "C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\Mapped_Images"
    for path in os.listdir(dir_path):
        mapped_im_list.append(dir_path + "\\" + path)

    stack_tifs(mapped_im_list)


    # store mapped image in file location
    write_to_dir(output_dir, morphed_image_set)



    """
    The code to test select cases
    image_path_1 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030022.tif'
    image_path_2 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030013.tif'
    image_path_3 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030035.tif'
    image_path_4 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030055.tif'
    image_path_5 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030063.tif'
    image_path_6 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030074.tif'
    image_path_7 = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030098.tif'

    image_testing(image_path_1, '1')
    image_testing(image_path_2, '2')
    image_testing(image_path_3, '3')
    image_testing(image_path_4, '4')
    image_testing(image_path_5, '5')
    image_testing(image_path_6, '6')
    image_testing(image_path_7, '7')
    """

#  [main]

def stack_tifs(mapped_images):
    """
    print("entered stack tifs method")
    list_file = all_images
    with TiffImagePlugin.AppendingTiffWriter("./test.tiff", True) as tf:
        for tiff_in in list_file:
            with open(tiff_in) as tiff_in:
                im = Image.open(tiff_in)
                im.save(tf)
                tf.newFrame()
    print(type(tf))
    """

    # cv.imread(mapped_images[0])
    cv.imshow("First Image", mapped_images[0])
    # Open the first TIFF image
    with Image.open(mapped_images[0]) as first_image:
        # Save the first image to a new file (this will be the destination file)
        print(type(first_image))
        first_image.save("output.tif", save_all=True)

    # Iterate over the remaining TIFF files starting from the second one
    for tiff_file in mapped_images[1:]:
        # Open each TIFF file
        with Image.open(tiff_file) as image:
            # Append the image to the destination file
            first_image.save("output.tif", append=True, save_all=True)




"""
"""
def write_to_dir(directory, dictionary):
    os.chdir(directory)
    for key, value in dictionary.items():
        cv.imwrite(value[0], value[1])


"""

"""
def find_filename(file):
    # Read filename
    filename = os.fsdecode(file)

    # Split the name into the name and extension
    split_tup = os.path.splitext(filename)

    # Create file extension variable
    file_extension = split_tup[1]

    return filename

def find_filepath(file):
    file_path = os.path.abspath(file)
    print(file_path)
    tokens = file_path.split('Napari Code')
    print(tokens)
    new_file_path = tokens[0] + 'Napari Code\JW_R03_nerve_stack' + tokens[1]
    final_file_path = new_file_path.replace('\\', '\\\\')
    return final_file_path

"""
Calculates the number of files in a directory
The dir_path variable is the path to the directory in question
"""
def dir_size(dir_path):
    count = 0
    for path in os.scandir(dir_path):
        if path.is_file():
            count += 1
    print('file count:', count)
    return count

"""
This method takes an image path and a string. It imports the file into an image
and shows the original image. It then calls plot lines.
"""
def image_testing(image_path, number_str):
    temp_image = cv.imread(image_path, cv.IMREAD_COLOR)
    print(type(temp_image))
    #cv.imshow(number_str, temp_image)

    return plot_lines(temp_image)

'''
This method converts the image to gray scale with proper weights in brightness
and contrast. 
'''
def contrast_image_v1(image):
    brightness = -20
    # Adjusts the contrast by scaling the pixel values by 0.5
    contrast = 0.5
    image2 = cv.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)
    return image2

# If we cant get napari points, we can save the copy of
# the image with the lines over it and display that copy
# OG parameters: def plot_lines(directory, image, image_name):
"""
This method creates a contrasted image of the image variable and shows that
new copy. It then converts it to gray scale and searches for edges in the 
image. Binary thresholding is then applied, followed by line detection on the
binary image. Afterwards it then draws those lines (contours) in green and 
displays the final image.
"""
def plot_lines(image):
    # print(type(image))
    print("Entered plot_lines")
    # Convert image to grayscale
    image_copy = contrast_image_v1(image)
    # cv.imshow("Image copy", image_copy)
    # cv.waitKey(0)
    gray = cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY)

    # Use canny edge detection
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    # apply binary thresholding
    ret, thresh = cv.threshold(edges, 150, 255, cv.THRESH_BINARY)
    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
    # draw contours
    cv.drawContours(image=image, contours=contours, contourIdx=-1, color=(224, 255, 255), thickness=2, lineType=cv.LINE_AA)
    # cv.imshow("Final Practice Image", image)
    # cv.waitKey(0)
    return image


'''
This method checks that the given path exists and acts accordingly
'''
def directory_set_up(path):
    if(os.path.exists(path)):
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
    else:
        # create new directory for new images
        os.makedirs(path)


"""
This method stores an image in a directory
"""
def store_new_image(directory, image_name, image):
    cv.imwrite(directory + 'analyzed_' + image_name, image)


"""
Change the method to take an int n and replace 153 with n
(which will be the length of the image_stack) 
OR
calculate the # of files in the directory beforehand or in 
the beginning of the method

This method takes a directory/file path and creates an array 
of the images in said directory. 
"""
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


"""
Main method
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()