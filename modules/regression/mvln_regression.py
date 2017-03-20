'''
AUTHOR : BAHRA Mehdi 
Python inplementation of multivariate linear regression 
this class represent a multivariate linear regression object with 
the mean squared error cost function and a  hypothesis with a specific degree of plolynomial 
the minimizer function can use vary optimization method such as gradient descent , normal equation for linear hypothesis
and conjugate gradient descent , this module send a report that will be used by another module to monitor the execution.



'''
import sys 
import numpy as np
import learning.util.optimization.GradientDescent as gd 

class Multivariate_linear_regression:
     def __init__(self,X,Y,optim={'method' : 'gd' , 'steps' : 100 , 'alpha' : 0 },extra_parameters={'regParam' :0}):
      '''
      Construct an multivariate_ln_reg object , define the hypothesis , the cost function and the gradient 
      '''

      #Add the bias unit to the X matrix 
      #Define the weights matrices Theta with the size of the matrix X 
    
      

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
    




     def hypothesis(self):
         print(np.shape(np.dot(self.X,self.Theta)))
         return np.dot(self.X,self.Theta)


     def cost(self):
       '''
       cost function to minimize : mean squared error
       '''

       m = self.number_of_examples

       return (1/(2*m))*(np.sum( np.power( self.hypothesis() - self.Y , 2) ) )
      
     def gradient(self):

      m = self.number_of_examples
      print(m)
      regParam  = self.extra_parameters['regParam']
      for i in range(0,np.size(self.Theta,1)+1):
        print("i = ",i)
        self.grad[i,:] = (1/m)*np.dot(np.transpose(self.hypothesis()-self.Y),self.X[:,i])
        print(self.grad)
      return self.grad



     def minimize_cost(self):
      if self.optim['method'] ==  'gd':
        print("minimizing")
        m = self.number_of_examples
        gd.gradient_descent(self.Theta,steps = self.optim['steps'],alpha = self.optim['alpha'] ,cost_function = self.cost, grad = self.gradient)
        
         
     def execute(self):
      pass





    