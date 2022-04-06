from math import inf


class Gen:

    def __init__(self, name):
        self.currentState = None
        self.name = name
        self.inputEvent = []

    def init(self):
        self.currentState = 0

    def internal(self):
        if self.currentState == 0:
            self.currentState = 0

    def external(self):
        pass

    def avancement(self):
        if self.currentState == 0:
            return 2.0
        return -1

    def generateOutput(self):
        if self.currentState == 0:
            return {"job": True}  #Reformat
