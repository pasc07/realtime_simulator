from math import inf

from Component import Component
from Const.Const import INTEGRAL, INTEGRALDQ


class IntegralDT(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.sign = 1.0
        self.initialValue = 0.0
        self.step = 0.01
        self.buffer = {}
        self.Integral = 0.0
        self.outputs = 'integral'
        self.attenuation = 1.0
        self.bounceIntegValue = 10.0

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
            Component.write(self, self.name, self.integral())
            print("Output generate INTEGRAL")
            return {INTEGRAL: True}  # Return a dict

    def integral(self):
        print(f'Buffer {self.name}   : {self.buffer}')
        new_value = list(self.buffer.values())
        if new_value:
            print(f'new_value = {new_value[0]}')
            self.Integral += (new_value[0] * self.step)
        print(f'IntegralDT = {self.Integral}')
        return self.Integral

    def conflict(self):
        self.external()

    def changeSign(self):
        if self.Integral < 0.0:
            self.bounceIntegValue = -self.Integral
            self.Integral = self.bounceIntegValue*self.attenuation


class IntegralDQ(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.buffer = {}  # Buffer to save events
        self.Integral = 0.0
        self.dt = inf
        self.dQ = 0.01  # Quantum de integral
        self.last_derivative = 0.0
        self.outputs = 'integralDQ'
        self.initialValue = 0.0

    def init(self):
        self.currentState = 0

    def internal(self):
        pass

    def external(self):
        if self.currentState == 0 and self.inputEvents:
            print(f'inputEvent {self.name} : {self.inputEvents}')
            self.buffer.update(self.inputEvents)
            # update dt
            self.updateDt()
            self.currentState = 0.0
            print(f'Current state Integral : {self.currentState}')

    def avancement(self):
        if self.currentState == 0:
            print(f'dt {self.name} = {self.dt}')
            return self.dt
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            val = self.integral()
            Component.write(self, self.name, val)
            print(f"Output generate {self.name}: {val}")
            return {INTEGRALDQ: True}  # Return a dict

    def updateDt(self):
        new_value = list(self.buffer.values())
        self.last_derivative = new_value[0]
        print(f'++++ last derivative = {self.last_derivative}')
        self.dt = self.dQ / abs(self.last_derivative)
        return self.dt

    def integral(self):
        print(f'Buffer {self.name}   : {self.buffer}')
        if self.last_derivative >= 0.0:
            self.Integral += self.dQ
        else:
            self.Integral -= self.dQ
        print(f'{self.name}= {self.Integral}')
        return self.Integral

    def conflict(self):
        self.external()
