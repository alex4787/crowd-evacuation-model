import numpy as np
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):
        self.graphX = [0]
        self.graphY_prey = [0]
        self.graphY_plant = [0]
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.line_prey, = self.ax.plot(self.graphX, self.graphY_prey, color="blue")
        self.line_plant, = self.ax.plot(self.graphX, self.graphY_plant, color="green")

    def update(self, num_tick, num_prey, plant_SA):
        self.graphX.append(num_tick)
        self.graphY_prey.append(num_prey)
        self.graphY_plant.append(plant_SA)
        self.line_prey, = self.ax.plot(self.graphX, self.graphY_prey, color="blue")
        self.line_plant, = self.ax.plot(self.graphX, self.graphY_plant, color="green")
        self.fig.canvas.draw()