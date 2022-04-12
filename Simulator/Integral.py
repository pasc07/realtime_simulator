
from Component import Component


class Integral(Component):

    def __init__(self,name):
        Component.__init__(self, name)
        self.integral=0.0
        self.step = 0.00001

    def init(self):
       pass

    def internal(self):
        if self.currentState == 0:
            self.currentState = 0

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return self.step
        return -1



    def generateOutput(self):
        if self.currentState == 0:
            self.integral += self.intputEvents.values()*self.step
            Component.write(self, "integral", self.integral)

    def conflict(self):
        pass