from math import inf

from Component import Component
from Const.Const import JOB


class Gen(Component):

    def __init__(self, name):
        Component.__init__(name)
        self.currentState = None
        self.inputEvent = []

    def init(self):
        self.currentState = 0

    def internal(self):
        if self.currentState == 0:
            self.currentState = 0

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return 2.0
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            return {JOB: True}  #Reformat
