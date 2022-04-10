from math import inf

from Component import Component
from Const.Const import FREE, BUSY, REQ, DONE


class Proc(Component):


    def __init__(self, name):
        Component.__init__(self, name)
        self.inputs = [REQ]
        print(f'inputs at Creation: {self.inputs}')

    def init(self):
        self.currentState = FREE

    def internal(self):
        if self.currentState == BUSY:
            self.currentState = FREE
        print(f'current State: {self.currentState}')

    def external(self):
        print(f'inputEvents{self.name}: {self.inputEvents}')
        if self.currentState == FREE and REQ in self.inputEvents:
            # self.inputEvents = {}
            self.currentState = BUSY
            print(f'current State: {self.currentState}')
        self.inputEvents.clear()

    def avancement(self):
        if self.currentState == FREE:
            return inf
        else:
            if self.currentState == BUSY:
                return 3.0
        return -1

    def generateOutput(self):
        if self.currentState == BUSY:
            self.write(DONE, True)
            print("Output generate DONE")
            return {"done": True}

    def conflict(self):
        self.internal()
