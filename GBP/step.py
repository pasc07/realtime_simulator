from math import inf

from Component import Component


class Step(Component):

    def __init__(self, name, xi, xf, ts):
        Component.__init__(self, name)
        self.xi = xi
        self.xf = xf
        self.ts = ts

    def init(self):
        self.currentState = 0

    def internal(self):
        print(f'current State (step): {self.currentState}')
        if self.currentState == 0:
            self.currentState = 1
        print(f'current State (step): {self.currentState}')

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return self.ts
        elif self.currentState == 1:
            return inf

    def generateOutput(self):
        if self.currentState == 0:
            self.write(f"xi_{self.name}", self.xi)
            print(f"Output generate {self.name} xi = {self.xi}")
        elif self.currentState == 1:
            self.write(f"xf_{self.name}", self.xf)
            print(f"Output generate {self.name} xf = {self.xf}")

    def conflict(self):
        pass