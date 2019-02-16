#this demonstrates the use of scikit learn as sklearn
#python data science
#created by ikon beth
#DevCUyo100DaysOfCode

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_boston, make_classification, make_circles, make_moons

#Iris dataset
data = load_iris()
x = data['data']
y = data['target']
y_labels = data['target_names']
x_labels = data['feature_names']

print('1st is ', x.shape)
print('2nd is ', y.shape)
print('3rd is', x_labels)
print('4th is ', y_labels)

#boston dataset
data = load_boston()
x = data['data']
y = data['target']
x_labels = data['feature_names']

print()
print('6th is', x.shape)
print('7th is', y.shape)
print('8th is', x_labels)

#make some classification dataset
x,y = make_classification(n_samples=50, n_features=5, n_classes=2)
print()
print('10th is', x.shape)
print('11th is', y.shape)
print ('12th is ', x[1,:])
print('13th is ', y[1])


x,y = make_circles()
plt.close('all')
plt.figure(1)
plt.scatter(x[:,0], x[:,1], c=y)


x,y = make_moons()
plt.figure(2)
plt.scatter(x[:,0],x[:,1],c=y)

plt.show()
