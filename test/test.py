import sys 
sys.path.append("/Users/mac/Desktop/project/")
import numpy as np
import learning.modules.regression.mvln_regression as mvlnreg 
import matplotlib.pyplot as plt

nbr_ligne= 0
i=0
with open("ex1data1.txt","r") as mon_fichier:
	contenu = mon_fichier.read()
	mes_lignes=contenu.split("\n")
	X = np.zeros(shape = (len(mes_lignes),1), dtype = float)
	Y = np.zeros(shape = (len(mes_lignes),1), dtype = float)
	for ligne in mes_lignes:
		words=ligne.split(",")
		X[i,:] = float(words[0])
		Y[i,:] = float(words[1])
		i+=1



plt.figure(1)


plt.axis([5, 25, -5, 25])


max_X = np.max(X[1,:])
min_X = np.min(X[1,:])



A = mvlnreg.Multivariate_linear_regression(X,Y,optim={'method' : 'gd' , 'steps' : 1500 , 'alpha' : 0.01 },extra_parameters={'regParam' :1})
A.minimize_cost()





print(A.Theta)

plt.plot(X, Y,'ro',X,A.hypothesis(),'k')
plt.show()




