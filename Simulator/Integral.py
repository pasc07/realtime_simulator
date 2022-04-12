from math import inf

from scipy import integrate as intg

from Component import Component
from Const.Const import INTEGRAL, INTEGRALDQ


class IntegralDT(Component):

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
        print(f'IntegralDT = {self.Integral}')
        return self.Integral

    def conflict(self):
        pass


class IntegralDQ(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.buffer = {}  # Buffer to save events
        self.Integral = 0.0
        self.dt = inf
        self.dQ = 0.01  # Quantum de integral
        self.last_derivative = 0.0

    def init(self):
        self.currentState = 0

    def internal(self):
        pass

    def external(self):
        if self.currentState == 0 and self.inputEvents:
            print(f'inputEvent Integral : {self.inputEvents}')
            self.buffer.update(self.inputEvents)
            # update dt
            self.updateDt()
            self.currentState = 0.0
            print(f'Current state Integral : {self.currentState}')

    def avancement(self):
        if self.currentState == 0:
            return self.dt
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            Component.write(self, INTEGRALDQ, self.integral())
            print("Output generate INTEGRALDQ")
            return {INTEGRALDQ: True}  # Return a dict

    def updateDt(self):
        new_value = list(self.buffer.values())
        self.last_derivative = new_value[0]
        print(f'++++ {self.last_derivative}')
        self.dt = self.dQ / abs(self.last_derivative)
        return self.dt

    def integral(self):
        if self.last_derivative >= 0.0:
            self.Integral += self.dQ
        else:
            self.Integral -= self.dQ
        print(f'IntegralDQ = {self.Integral}')
        return self.Integral

    def conflict(self):
        self.external()
