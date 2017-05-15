import sys
sys.path.append("/Users/mac/Desktop/project/")
import os
from scipy import ndimage
import numpy as np
import pickle
import learning.util.normalization.data_normalization as dn
from random import randint
import matplotlib.pyplot as plt
import learning.modules.regression.lg_classification as lgc
import matplotlib.image as mpimg


'''
Test script of multiclass logistic regression/classification using the datamnist images 
of charchter A to Z
'''

#loading images , shuffle them and make our training set , each example have width*height features

# We have to split our data set to three other data set for cross validation, a validation set , and a test set
# The 


images_folder = "./notMNIST_small"

def sigmoid(x):
 	return 1/(1+np.exp(-x))
def hypothesis(x,theta):
	h= sigmoid(np.dot(x,theta))
	print('hypothesis :' , h)
	return h



X = []
labels = ['A','B','C','D','E','F','G','H','I','J']

image_size = 28
datasets = {}
dataset_label = None
label = None
cpt = 0
MAX_IMG_BY_LABEL = 500

if not os.path.exists('datasets.pkl') and not os.path.exists('labels.pkl') :
	for dir_label in os.listdir(images_folder):
		cpt1= 0
		print("dir label ",dir_label)
		if dir_label in labels:
			print(dir_label)
			if dataset_label == None:
				dataset_label =  np.ndarray(shape=(5000, image_size, image_size),dtype= float)
				label = np.ndarray(shape=(5000) , dtype=np.dtype('a1'))
				print('Mark 1',label.shape[0]==dataset_label.shape[0])
			else:
				dataset_label.resize((5000,image_size,image_size))
				label.resize((5000))
			label_folder  =  os.path.join(images_folder,dir_label)
			for image_file in os.listdir(label_folder):
				#get the image normalize it  and store it into the dataset
				image_file = os.path.join(label_folder,image_file)
				print(image_file)
				try:
					if cpt1 == MAX_IMG_BY_LABEL:
						break
					img_data= ndimage.imread(image_file).astype(float)
					print(img_data.shape)
					print(img_data.shape)
					print(dir_label)
					dataset_label[cpt,:,:] = img_data
					label[cpt] = dir_label
					cpt+=1
					cpt1 += 1
				except Exception as e:
					label.resize((label.shape[0] - 1))
					dataset_label.resize((dataset_label.shape[0] - 1),image_size,image_size)
					print('img read failed')
				
	print(dataset_label)
	print('##counter',cpt)
	datasets_file  = open('datasets.pkl','wb')
	pickle.dump(dataset_label, datasets_file)
	datasets_file.close()
	print(dataset_label)
	print(len(dataset_label))
	labels_file  = open('labels.pkl','wb')
	pickle.dump(label, labels_file)
	datasets_file.close()



print('open datasets')


datasets_file = open('datasets.pkl','rb') 

#unpickle dataset
datasets = pickle.load(datasets_file)

datasets_file.close()


labels_file = open('labels.pkl','rb')
labels = pickle.load(labels_file)
print('####labels',labels)
labels_file.close()


print('### equal size',datasets.shape[0] == labels.shape[0])

print(labels.shape[0])
print(datasets.shape[0])

X = np.zeros(shape =(datasets.shape[0],28,28))
Y = np.ndarray(shape =(datasets.shape[0],1) , dtype= np.dtype('a1'))

# shuffle the data
if not os.path.exists('X.pkl') and not os.path.exists('Y.pkl'):
	print(X.shape == datasets.shape)
	cpt = 0
	index_full = []
	i = 0
	while i < (datasets.shape[0] - 1):
		while True : 
			index = randint(0,datasets.shape[0]-1)
			if index not in index_full:
				index_full.append(index)
				break
		X[index,:,:]  = datasets[i,:,:]
		print(labels[i])
		Y[index] = labels[i]
		i += 1

	features = open('X.pkl','wb')
	pickle.dump(X, features)
	features.close()
	labels = open('Y.pkl','wb')
	pickle.dump(Y, labels)
	labels.close()

labels_file = open('Y.pkl','rb')
Y = pickle.load(labels_file)
features_file = open('X.pkl','rb')
features = pickle.load(features_file)

print(Y)

labels_file.close()
print(Y[5,0])
plt.imshow(features[5])
print('nombre de ',Y[5,0], 'is' ,np.where(Y[:,0] == Y[5,0])[0].shape)


cpt = 0
X = np.zeros(shape =(features.shape[0],28*28))
for feature in features:
	# reshape
	X[cpt,:] = feature.reshape((28*28))
	cpt += 1

print(X)
print(X[1].shape)

Thetas = {}
labels_name = ['A','B','C','D','E','F','G','H','I','J']
'''for label in labels_name:
	# run the logistic regression

	Y_encoding = np.ndarray((X.shape[0],1),dtype=np.int)
	label_array = np.full((X.shape[0],1),label,np.dtype('a1'))
	print(label_array)
	Y_encoding = (Y==label_array)
	Y_encoding = Y_encoding.astype(np.float64)
	print('nombre de ',label, 'is' ,np.where(Y_encoding[:,0] == 1)[0].shape)

	dn.normalize_data(X)
	print(X)
	print(Y_encoding)
	A = lgc.logistic_classification(X,Y_encoding,optim={'method' : 'cg' , 'steps' : 50 , 'alpha' : 0.01},extra_parameters={'regParam' :0.1})
	Theta_label = A.minimize_cost()
	Thetas[label] = Theta_label



#pickle the object A

A_file= open('A.pkl','wb')
pickle.dump(Thetas, A_file)
A_file.close()'''


# predict image after training
Thetas_file = open('A.pkl','rb')
Thetas = pickle.load(Thetas_file)

# read X
X = np.concatenate((X,np.ones(shape=(np.size(X,0),1), dtype = np.float64 )),axis=1)
x_to_predict = X[4999,:]
y_to_predict = np.char.decode(Y[4999,0])
print(str(y_to_predict))
hypothesis(x_to_predict,Thetas[str(y_to_predict)])
plt.imshow(features[4999])
plt.show()







