# importing the libraries
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Next the path to the precropped card images that will be used in the data set.
path = 'C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\src\\scryfall_artcrops'

# Build the training data ensuring the correct sizing and color mode.
training_data = []
for img in os.listdir(path):
    pic = cv2.imread(os.path.join(path,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(80,80))
    training_data.append([pic])

# Create and save the training list as numpy array for the training data
np.save(os.path.join(path,'features'),np.array(training_data))