import sys 
import numpy as np
import itertools

def normalize_data(X):
	
	#get each row of feature , and normalize each element , compute first the mean of the row and the standard deviation and normalize each feature

	for row_feature in np.transpose(X):
		#Compute the mean
		mean_row = np.mean(row_feature)
		#Compute the deviation
		deviation_row = np.std(row_feature)
		row_feature -= mean_row
		row_feature /=deviation_row



def add_poly_feature(X , degree = 1):
	#get the number of features 
    new_features =[]
    #print(list(np.transpose(X)))
    combinations = list(itertools.combinations_with_replacement(list(np.transpose(X)),degree))
    for combination in combinations:
    	#convert combination into a nd array and compute the  prod
    	new_features.append(np.prod(np.array(combination,dtype =float),axis=0))
    return np.concatenate((X,np.transpose(np.array(new_features ,dtype = float))),axis=1)


