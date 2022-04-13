from math import inf

from Component import Component
from Const.Const import STEP


class Step(Component):

    def __init__(self, name, xi, xf, ts):
        Component.__init__(self, name)
        self.xi = xi
        self.xf = xf
        self.ts = ts
        self.outputs = 'step'

    def init(self):
        self.currentState = 0

    def internal(self):
        print(f'current State (step): {self.currentState}')
        if self.currentState == 0:
            self.currentState = 1
            print(f'current State (step): {self.currentState}')
        elif self.currentState == 1:
            self.currentState = 2
            print(f'current State (step): {self.currentState}')
        elif self.currentState == 2:
            self.currentState = 2
            print(f'current State (step): {self.currentState}')

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return 0.0
        elif self.currentState == 1:
            return self.ts
        elif self.currentState == 2:
            return inf

    def generateOutput(self):
        if self.currentState == 0:
            self.write(f"{self.name}", self.xi)
            print(f"Output generate {self.name} xi = {self.xi}")
        elif self.currentState == 1:
            self.write(f"{self.name}", self.xf)
            print(f"Output generate {self.name} xf = {self.xf}")

    def conflict(self):
        self.internal()