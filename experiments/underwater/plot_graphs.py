from types import LambdaType
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

def plot_height_both():
    f_air = open('experiments/underwater/air_heights.txt').read()
    f_water = open('experiments/underwater/water_heights.txt').read()

    y_air = [float(i) for i in f_air.split('\n')[:-1]]
    y_water = [float(i) for i in f_water.split('\n')[:-1]]
    x = np.linspace(0,20, len(y_air))
    plt.plot(x, y_air, label = 'No buoyancy')
    plt.plot(x, y_water, label = 'Buoyancy')
    plt.title('Height over time of a falling spider bot with and without buoyancy')
    plt.grid()
    plt.ylabel('Height in meters')
    plt.xlabel('Time in seconds')
    plt.legend()
    plt.savefig('experiments/underwater/both_plot.png')

def plot_velocity(type):
   with open('experiments/underwater/'+type+'_velocities.txt') as f:
        data = f.read()
        y = [float(i) for i in data.split('\n')[:-1]]
        x = np.linspace(0,20, len(y))
        plt.plot(x, y)
        plt.title('Velocity over time of a falling spider bot in ' + type)
        plt.grid()
        plt.ylabel('Velocity in meters per second')
        plt.xlabel('Time in seconds')
        plt.savefig('experiments/underwater/'+type+'_velocity_plot.png')

plot_height_both() 