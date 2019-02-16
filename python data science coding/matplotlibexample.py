#this demonstrate the use of both numpy and matplotlib in plotting \
#both line ans scattter diagrams
#python data science
#created by ikon beth
#DevCUyo100DaysOfCode




import numpy as np
import matplotlib.pyplot as plt

def simple_line_plot(x,y,figure_no):
    plt.figure(figure_no)
    plt.plot(x,y)
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.title('Simple Lines')

def simple_dots(x,y,figure_no):
    plt.figure(figure_no)
    plt.plot(x,y,'or')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.title('Simple Dots')

def simple_scatter(x,y,figre_no):
    plt.figure(figure_no)
    plt.scatter(x,y)
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title('Simple Scatter')

def scatter_with_color(x,y,figure_no):
    plt.figure(figure_no)
    plt.scatter(x,y)
    plt.xlabel('x-labels')
    plt.ylabel('y-labels')
    plt.title('Scatter with color')

if __name__ == "__main__":
    plt.close('all')
    #sample x y data for simple line and dot plots
    x= np.arange(1,100,dtype=float)
    y= np.array([np.power(xx,2) for xx in x])

    figure_no = 1
    simple_line_plot(x,y,figure_no)
    figure_no += 1
    simple_dots(x,y,figure_no)

    #sample data for scatter plots with and without color
    x = np.random.uniform(size=100)
    y = np.random.uniform(size=100)

    figure_no += 1
    simple_scatter(x,y,figure_no)
    figure_no += 1
    scatter_with_color(x,y,figure_no)
    plt.show()

    
    
    
    
