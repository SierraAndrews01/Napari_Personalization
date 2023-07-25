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


# The commented out section individual prints out all the images and you have to select each image to
# view it
"""

viewer = napari.Viewer()
counter = 0
directory = 'C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\JW_R03_nerve_stack'
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)

    split_tup = os.path.splitext(filename)
    print(split_tup)

    file_extension = split_tup[1]
    print("File Extension: ", file_extension)

    if file_extension != ".tif":
        print("Fraud")
        print(counter)
        counter = counter + 1
    elif file_extension == "":
        counter = counter + 1
    else:
        tif_path = directory + '\\' + filename
        image = tifffile.imread(tif_path)

        # Convert the image to a NumPy array
        image_array = np.array(image)

        new_layer = viewer.add_image(image_array)

        # Now you can work with the image array as a NumPy array
        # For example, you can access its shape, perform operations, etc.
        print(image_array.shape)

        counter = counter + 1
        print(counter)

napari.run()
"""
directory = 'C:\\Users\\andrewss\\PycharmProjects\\pythonProject\\JW_R03_nerve_stack'
viewer = napari.Viewer()
counter = 0
photo_arrays = list() * 153
print(photo_arrays)

for file in os.listdir(directory):
    print("---------------------------------------------------------------------------------------------")
    # Read filename
    filename = os.fsdecode(file)
    print(filename)

    # Split the name into the name and extension
    split_tup = os.path.splitext(filename)
    print(split_tup)

    # Create file extension variable
    file_extension = split_tup[1]
    print("File Extension: ", file_extension)

    # Creates the list that the images (as arrays) are stored in

    # If the extension is not a TIFF file it ignores it and prints/increments the counter
    #if file_extension != ".tif":
     #   print("Fraud")
     #   print(counter)
    #    counter = counter + 1
    if counter <= 6:
        print(counter)
        counter = counter + 1
    # If the file doesn't have an extension it ignores it and prints/increments the counter
    #elif file_extension == "":
       # counter = counter + 1
    # If it is a TIFF file it creates a path for it, reads the image, and converts
    # it to a numpy array that is then added to a list
    else:
        # Creates file directory
        tif_path = directory + '\\' + filename
        image = tifffile.imread(tif_path)

        # Convert the image to a NumPy array
        image_array = np.array(image)
        print(image_array)

        # Stores photo array in list
        photo_arrays.append(image_array)

        print(len(photo_arrays))

        print(counter)
        counter = counter + 1
        print("-----------------------------------------------------------------------------------------")
print(type(photo_arrays))
print(len(photo_arrays))
print(photo_arrays)

nparry = np.array(photo_arrays)

print(nparry.shape)
new_layer = viewer.add_image(nparry)
new_layer.colormap = 'green'
napari.run()
