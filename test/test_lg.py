import sys 
sys.path.append("/Users/mac/Desktop/project/")
import numpy as np
import learning.modules.regression.mvln_regression as mvlnreg 
import learning.modules.regression.lg_classification as lgc
import learning.util.normalization.data_normalization as dn
import matplotlib.pyplot as plt

#initial counter
i = 0
with open("ex2data2.txt","r") as mon_fichier:
	contenu = mon_fichier.read()
	mes_lignes=contenu.split("\n")
	X = np.zeros(shape = (len(mes_lignes),2), dtype = float)
	Y = np.zeros(shape = (len(mes_lignes),1), dtype = float)
	for ligne in mes_lignes:
		words=ligne.split(",")
		len(words)
		X[i,0] = float(words[0])
		X[i,1] =float(words[1])
		Y[i,:] = float(words[2])
		i+=1


original_X = X
dn.normalize_data(X)
print('######AFTER POLY ########');
print(X)

X = dn.add_poly_feature(X,degree=8)
print('######BEFORE POLY ########');
print(X)
print(Y)
input()
#A = lgc.logistic_classification(X,Y,optim={'method' : 'cg' , 'steps' : 100000 , 'alpha' : 0.1 },extra_parameters={'regParam' :0})

#print(A.hypothesis())

'''max_X = np.max(X[0,:])+2
min_X = np.min(X[0,:])-2

boundaries = (-1/(A.Theta[1,:]))*(A.Theta[2,:]+(A.Theta[0,:]*np.array([min_X,max_X])))
print("boundary : ",boundaries)
#print("cost function : ",A.cost_function())
print("Theta :",A.Theta)'''
A.minimize_cost()
u = np.linspace(-1, 1.5, 50)
v = np.linspace(-1, 1.5, 50)
u = np.array(u , dtype = float)
u = u.reshape((np.size(u,0),1))
v = np.array(v, dtype = float)
v = u.reshape((np.size(v,0),1))

X_test =np.concatenate((u,v),axis=1)

z = np.zeros(shape=(np.size(u,0),np.size(v,0)) , dtype=float)


for i in range(0,len(u)):
	for j in range(0,len(v)):
		temp = np.array((u[i,0],v[j,0]),dtype=float)
		temp = temp.reshape((1,2))
		z[i,j] = np.concatenate((dn.add_poly_feature(temp,degree=8),np.ones(shape=(np.size(temp,0),1),dtype = float)),axis=1).dot(A.Theta)



#x_boundary = np.array([min_X,max_X])
plt.figure(1)

plt.axis([-1, 1.5, -1, 1.5])

pos = np.where(Y==1)


neg =  np.where(Y==0) 

plt.plot(original_X[pos,0], original_X[pos,1],'g+',original_X[neg,0], original_X[neg,1],'ro')
u = np.linspace(-1, 1.5, 50)
v = np.linspace(-1, 1.5, 50)
u, v= np.meshgrid(u,v)
plt.contourf(u,v,np.transpose(z),[0,0.02],colors='r')
#print(A.cost_function().shape)
plt.show()

