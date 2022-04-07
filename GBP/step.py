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
            self.write("xi", self.xi)
            print("Output generate xi")
        elif self.currentState == 1:
            self.write("xf", self.xf)
            print("Output generate xf")
