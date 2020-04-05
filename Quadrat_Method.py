#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Libraries required
# =============================================================================

import matplotlib.pyplot as plt # should install with python
import matplotlib.patches as patches # should install with python
from PIL import Image # pip install Pillow
import numpy as np # should come with python
import random # pip install random

# =============================================================================
# The function
# =============================================================================

def add_square(imp):

	# This function adds a quadrat randomly on top of the image supplied.
	# Adding multiple quadrats to an image allows for the random comparison of 
	# different image sections.

    # The Image

    im = np.array(Image.open(imp), dtype=np.uint8) # Loading in image as matrix array
    fig,ax = plt.subplots(1) # Create figure and axes
    ax.imshow(im) # Display the image
    
    # Create a Quadrat Rectangle Patch

    rec_len = int(len(im)/10) # Lenght of quadrat. Currently set to 1/10th the Image size
    rec_width = int(len(im[0])/10) # Witdh of quadrat. Currently set to 1/10th the image size
    
    x_overlap = int(len(im)-rec_len) # Stop quatrat going out of bounds of image
    y_overlap = int(len(im[0])-rec_width) # Stop quadrat going out of bounds of image
    
    x = random.randint(0,x_overlap) # Random x position of quadrat
    y = random.randint(0,y_overlap) # Random y position of quadray
    
    rect = patches.Rectangle((x,y),rec_len,rec_width,
                             linewidth=2,edgecolor='r',facecolor='none') # Creating quadrat
    
    # Adding the quadrat patch to the Image

    ax.add_patch(rect) 
    
    plt.show() 

# =============================================================================
# The user 
# =============================================================================

add_square('Image_Name_Here.png')