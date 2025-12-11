import matplotlib.pyplot as plt
import numpy as np

def plot_hyperbola(a, b, N):
    x = np.arange(a, b, N) 
    y = [1/i for i in x]
    plt.plot(x, y, color= 'green', label= 'hyperbola')
    plt.title('my hyperbola')
    plt.legend()
    plt.savefig('fig_task1.png')
if __name__ == '__main__':
    plot_hyperbola(-10, 10, 1)
