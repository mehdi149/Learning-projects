'''

Python implementation of  logistic classification using various optimization technique

Gradient descent and conjugate gardient descent 


Author : BAHRA Mehdi



'''


import sys
import os
import numpy as np
import learning.util.optimization.GradientDescent as gd 
from scipy import optimize






class logistic_classification:
      ##Todo:
      #Extend this implementation to multiclass classification , take labels parameters , evaluate the length , make one hot encoding
      #and perform logistic classification for each class.

      ##TODO!
      #THIS IMPLEMENTATION WORK JUST WITH A 2 DIMENSIONAL STRUCTURE OF FEATURE , MAKE IT ABLE TO WORK WITH N DIMENSIONAL STRUCTURE TENSOR.
	def __init__(self,X,Y,optim={'method' : 'gd' , 'steps' : 100 , 'alpha' : 0 },extra_parameters={'regParam' :0}):
		#Add bias unit to our training examples 
		self.number_of_examples = np.size(X,0)
		self.X = np.concatenate((X,np.ones(shape=(np.size(X,0),1), dtype = float )),axis=1)
		self.number_of_features = np.size(X,1)
		print(self.X)
		print(np.size(self.X,1))
		self.Theta = np.zeros(shape= (np.size(self.X,1),1) , dtype = float)
		self.Y  = Y;
		self.grad = np.zeros(shape=self.Theta.shape , dtype = float)
		self.optim = optim

		self.extra_parameters = extra_parameters;

	def sigmoid(self,x):
 		return 1/(1+np.exp(-x))
	def hypothesis(self,x,theta):
		return self.sigmoid(np.dot(x,theta))



	def cost_function(self,*args):
		theta,x ,y = args
		print("x :",x)
		m = self.number_of_examples
		lamb_da = self.extra_parameters['regParam']
		return  - (1 / m) * (np.dot(np.transpose(y) , np.log(self.hypothesis(x,theta))) + np.dot(np.transpose(1 - y),np.log(1-self.hypothesis(x,theta))))+(lamb_da/(2*m))*(np.sum(np.power(theta[0:np.size(theta,0)-1],2)))


	def gradient(self,*args):
		theta, x , y= args
		#x = np.array(args[0])
		lamb_da =self.extra_parameters['regParam'] 
		theta = np.reshape(theta,(theta.shape[0],1))
		m = self.number_of_examples
		regParam  = self.extra_parameters['regParam']
		for i in range(0,np.size(theta,0)):
			if(i == np.size(theta,0)-1):
				self.grad[i,:] = (1/m)*np.dot(np.transpose(self.hypothesis(x,theta)-y),x[:,i])
			else:
				self.grad[i,:]=(1/m)*np.dot(np.transpose(self.hypothesis(x,theta)-y),x[:,i]) + ((lamb_da/m)*theta[i,:])



			
		#print("first gradient ",self.grad)
		#print(self.cost_function())
		#input()
		if(self.optim['method'] ==  'gd'):
			return self.grad
		else:
			return self.grad.flatten()

	def minimize_cost(self):
		if self.optim['method'] ==  'gd':
			print("minimizing")
			m = self.number_of_examples
			gd.gradient_descent(self.Theta,steps = self.optim['steps'],alpha = self.optim['alpha'] ,cost_function = self.cost_function, grad = self.gradient ,args = (self.Theta,self.X,self.Y))
		if self.optim['method'] ==  'cg':
			print("minimizing 2")
			theta = optimize.fmin_cg(self.cost_function, x0 = self.Theta, fprime=self.gradient,args=(self.X,self.Y),maxiter=1400)
			self.Theta = np.reshape(theta,self.Theta.shape)

        




