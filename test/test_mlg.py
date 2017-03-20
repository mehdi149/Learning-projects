import sys
sys.path.append("/Users/mac/Desktop/project/")
import os
from scipy import ndimage
import numpy as np
import pickle
import learning.util.normalization.data_normalization as dn

'''
Test script of multiclass logistic regression/classification using the datamnist images 
of charchter A to Z
'''

#loading images , shuffle them and make our training set , each example have width*height features

# We have to split our data set to three other data set for cross validation, a validation set , and a test set
# The 


images_folder = "./notMNIST_small"


X = []
labels = ['A','B','C','D','E','F','G','H','I','J']

image_size = 28


for dir_label in os.listdir(images_folder):

	if dir_label in labels:
		dataset_label =  np.ndarray(shape=(len(os.listdir(images_folder+'/'+dir_label)), image_size, image_size),dtype=np.float32)
		label_folder  =  os.path.join(images_folder,dir_label)
		cpt=0
		for image_file in os.listdir(label_folder):
			#get the image normalize it  and store it into the dataset
			image_file = os.path.join(label_folder,image_file)
			img_data= ndimage.imread(image_file).astype(float)
			dn.normalize_data(img_data)
            dataset_label[cpt,:,:] = img_data



		


