from math import inf

from Component import Component
from Const.Const import FREE, BUSY, REQ, DONE


class Proc(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        Component.inputs = [REQ]

    def init(self):
        self.currentState = FREE

    def internal(self):
        if self.currentState == BUSY:
            self.currentState = FREE

    def external(self):
        if self.currentState == FREE and REQ in self.inputEvents:
            # print(f'inputEvents: {self.inputEvents}')
            self.inputEvents = {}
            self.currentState = BUSY
            print(f'current State: {self.currentState}')

    def avancement(self):
        if self.currentState == FREE:
            return inf
        else:
            if self.currentState == BUSY:
                return 3.0
        return -1

    def generateOutput(self):
        if self.currentState == BUSY:
            Component.write(self, DONE, True)
            return {"done": True}
