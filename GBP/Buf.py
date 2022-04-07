from math import inf

from Component import Component
from Const.Const import JOB, A, B, C, DONE, REQ


class Buf(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        Component.inputs = [JOB, DONE]
        self.q = 0

    def init(self):
        self.currentState = A

    def internal(self):
        if self.currentState == B:
            self.currentState = A

    def external(self):
        if self.currentState == A and JOB in self.inputEvents:
            print(f'{JOB} is in inputEvents')
            self.currentState = B
            self.q += 1
        else:
            if self.currentState == B:
                self.q -= 1
                self.currentState = C
            else:
                if self.currentState == C and "job" in self.inputEvents:
                    self.q += 1
                    self.currentState = C
                else:
                    if self.currentState == C and "done" in self.inputEvents and self.q == 0:
                        self.currentState = A
                    else:
                        if self.currentState == C and "done" in self.inputEvents and self.q > 0:
                            self.currentState = B
        self.inputEvents = {}

    def avancement(self):
        if self.currentState == A:
            return inf
        else:
            if self.currentState == B:
                return 0.0
            else:
                if self.currentState == C:
                    return inf
        return -1

    def generateOutput(self):
        if self.currentState == B:
            Component.write(self, REQ, True)
            return {"req": True}  # Reformat
