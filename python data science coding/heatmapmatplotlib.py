#this demonstrates the use of numpy and matplotlib
#in generating heatmaps and labelling x and y axes
#python data science
#created by ikon beth
#DevCUyo100DaysofCode

import numpy as np
import matplotlib.pyplot as plt

def x_y_axes_labelling(x,y,x_labels,y_labels, figure_no):
    plt.figure(figure_no)
    plt.plot(x,y,'ob')
    plt.margins(0.2)
    plt.xticks(x,x_labels,rotation = "vertical")
    plt.yticks(y,y_labels,)

def plot_heat_map(n,figure_no):
    plt.figure(figure_no)
    plt.pcolor(n)
    plt.colorbar()

if __name__ == '__main__':
    plt.close('all')

    x = np.array(range(1,7))
    y = np.array(range(100,700,100))
    x_labels = ['element 1', 'element 2', 'element 3', 'element 4',
                'element 5', 'element 6', 'element 7']
    y_labels = ['weight 1', 'weight 2', 'weight 3', 'weight 4', 'weight 5',
                'weight 6', 'weight 7']

    x_y_axes_labelling(x,y,x_labels,y_labels,1)

    n = np.random.normal(loc=0.5, scale=0.2, size =(20,20))
    plot_heat_map(n,2)

    plt.show()
    
