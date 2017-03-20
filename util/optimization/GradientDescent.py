import numpy as np

def gradient_descent(initial_theta,steps = 0,alpha = 0,cost_function = None, grad = None ,args=()):
   print("steps : ",steps)
   print("ALPHA :",alpha)
   theta_temp = np.zeros(shape=initial_theta.shape,dtype= float)
   for i in range(0,steps):
   	 for j in range(0,np.size(initial_theta,0)):
   	 	theta_temp[j,:] = initial_theta[j,:] - alpha*grad(initial_theta,args[1],args[2])[j,:]
   	 initial_theta[:,:] = theta_temp[:,:]