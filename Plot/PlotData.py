import matplotlib.pyplot as plt
import numpy as np


class PlotData:

    def __init__(self, name):
        self.name = name
        self.xValue = []
        self.yValue = []

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

    def updateGraph(self):
        pass
