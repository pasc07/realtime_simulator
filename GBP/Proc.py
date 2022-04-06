from math import inf


class Proc:

    def __init__(self, name):
        self.currentState = None
        self.name = name
        self.inputEvent = []

    def init(self):
        self.currentState = 0

    def internal(self):
        if self.currentState == 1:
            self.currentState = 0

    def external(self):
        if self.currentState == 0 and "req" in self.inputEvents:
            self.currentState = 1

    def avancement(self):
        if self.currentState == 0:
            return inf
        else:
            if self.currentState == 1:
                return 3.0
        return -1

    def generateOutput(self):
        if self.currentState == 1:
            return "done", True  #Reformat
