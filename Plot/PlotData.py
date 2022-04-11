import time

import matplotlib.pyplot as plt
import numpy as np


class PlotData:

    def __init__(self, name):
        self.figure = None
        self.line1 = None
        self.name = name
        self.xValue = [0]
        self.yValue = [0]

    def addPoint(self, xValue, yValue):
        self.xValue.append(xValue)
        self.yValue.append(yValue)

    def plot_step(self):
        # Variable to draw figure
        xValue_array = np.asarray(self.xValue)
        yValue_array = np.asarray(self.yValue)

        x = xValue_array
        y = yValue_array
        print(x)
        print(y)
        # plt.step(x, y, label='pre (default)')
        # plt.plot(x, y, 'o--', color='grey', alpha=0.3)

        # plt.step(x, y + 1, where='mid', label='mid')
        # plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

        plt.step(x, y, where='post', label='post')
        plt.plot(x, y, 'o--', color='grey', alpha=0.3)

        plt.grid(axis='x', color='0.95')
        plt.legend(title='Parameter where:')
        plt.title('plt.step(where=...)')
        plt.show()

    def graphInit(self):
        plt.ion()
        # here we are creating sub plots
        xValue_array = np.asarray(self.xValue)
        yValue_array = np.asarray(self.yValue)
        self.figure = plt.figure()
        # ax = self.figure.add_subplot(111)
        self.figure, ax = plt.subplots(figsize=(8, 6))
        ax.set_ylim([-4, 5])
        ax.set_xlim([0, 5])
        self.line1, = ax.plot(xValue_array, yValue_array)

        # setting title
        plt.title("Discrete Simulation Graph", fontsize=20)

        # setting x-axis label and y-axis label
        plt.xlabel("Time elapsed")
        plt.ylabel("Values")

    def updateGraph(self):

        new_x = np.asarray(self.xValue)
        new_y = np.asarray(self.yValue)
        # updating data values
        self.line1.set_xdata(new_x)
        self.line1.set_ydata(new_y)

        # drawing updated values
        self.figure.canvas.draw()
        # This will run the GUI event
        # loop until all UI events
        # currently waiting have been processed
        self.figure.canvas.flush_events()

        time.sleep(0.1)
