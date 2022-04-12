from scipy import integrate as intg

from Component import Component
from Const.Const import INTEGRAL


class Integral(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.step = 0.01
        self.buffer = {}
        self.Integral = 0.0

    def init(self):
        self.currentState = 0

    def internal(self):
        pass

    def external(self):
        if self.currentState == 0 and self.inputEvents:
            print(f'inputEvent Integral : {self.inputEvents}')
            self.buffer.update(self.inputEvents)
            self.currentState = 0.0
            print(f'Current state Integral : {self.currentState}')

    def avancement(self):
        if self.currentState == 0:
            return self.step
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            Component.write(self, INTEGRAL, self.integral())
            print("Output generate INTEGRAL")
            return {INTEGRAL: True}  # Return a dict

    def integral(self):
        new_value = list(self.buffer.values())
        print(f'new_value = {new_value[0]}')
        self.Integral += new_value[0]*self.step
        print(f'Integral = {self.Integral}')
        return self.Integral

    def conflict(self):
        pass