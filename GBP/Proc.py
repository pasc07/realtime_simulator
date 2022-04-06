from math import inf

from Const.Const import FREE, BUSY


class Proc:

    def __init__(self, name):
        self.currentState = None  # ToDo Remove after
        self.name = name
        self.inputEvent = []  # ToDo define elsewhere

    def init(self):
        self.currentState = FREE

    def internal(self):
        if self.currentState == BUSY:
            self.currentState = FREE

    def external(self):
        if self.currentState == FREE and "req" in self.inputEvents:
            self.currentState = BUSY

    def avancement(self):
        if self.currentState == FREE:
            return inf
        else:
            if self.currentState == BUSY:
                return 3.0
        return -1

    def generateOutput(self):
        if self.currentState == BUSY:
            return {"done": True}  # in const
