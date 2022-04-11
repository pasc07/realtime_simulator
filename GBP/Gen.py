from math import inf

from Component import Component
from Const.Const import JOB, DONE


class Gen(Component):

    def __init__(self, name):
        Component.__init__(self, name)

    def init(self):
        self.currentState = 0

    def internal(self):
        if self.currentState == 0:
            self.currentState = 0
            print(f'current State: {self.currentState}')

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return 2.0
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            Component.write(self, JOB, True)
            print("Output generate JOB")
            return {JOB: True}  # Return a dict

    def conflict(self):
        self.external()
