import napari

# create a Viewer and add an image here
viewer = napari.view_image("Images/")

# custom code to add data here
viewer.add_points(my_points_data)

# start the event loop and show the viewer
napari.run()