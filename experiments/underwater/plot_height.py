import matplotlib.pyplot as plt
import numpy as np

def plot_height(type):

    with open('experiments/underwater/'+type+'_heights.txt') as f:
        data = f.read()
        y = [float(i) for i in data.split('\n')[:-1]]
        x = np.linspace(0,20, len(y))
        plt.plot(x, y)
        plt.title('Height over time of a falling spider bot in ' + type)
        plt.grid()
        plt.ylabel('Height in meters')
        plt.xlabel('Time in seconds')
        plt.savefig('experiments/underwater/'+type+'_plot.png')

#plot_height('water')