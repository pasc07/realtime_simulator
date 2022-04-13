from Component import Component


class Constante(Component):

    def __int__(self, name):
        Component.__init__(self, name)
        self.outputs = 'dv'
        self.g = float(-9.81)

    def init(self):
        self.currentState = 0

    def internal(self):
        pass

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return 0.0
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            self.write(self.outputs, self.g)
            print(f"Output generate {self.name} g = {self.g}")

    def conflict(self):
        pass