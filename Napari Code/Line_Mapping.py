from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse


def main():
    global src
    src = cv.imread('C:\\Users\\andrewss\\PycharmProjects\\Napari_Personalization\\Napari Code\\JW_R03_nerve_stack\\JW_R_030000_2022-09-13T11-11-45.333.tif')
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    if src is None:
        print('Could not open or find the image: ', src)
        exit(0)
    opened_image = cv.morphologyEx(src, cv.MORPH_OPEN, kernel)
    cv.imshow('Original Image', src)
    cv.imshow('Opened Image', opened_image)
    lines = plot_lines(opened_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
## [main]

def plot_lines(image):
    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Use canny edge detection
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    # Apply HoughLinesP method to
    # to directly obtain line end points
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
    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
    args = parser.parse_args()

    main()