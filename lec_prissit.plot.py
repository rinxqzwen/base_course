import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0):

    x = np.arrange(-10, 10, 0.01)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label='my parabola')   
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Parabola')
    plt.legend()
	
    plt.savefig('fig_4.png')