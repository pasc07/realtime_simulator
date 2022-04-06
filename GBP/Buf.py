from math import inf

from Component import Component
from Const.Const import JOB, A, B, C, DONE


class Gen(Component):

    def __init__(self, name):
        Component.__init__(name)
        self.input = [JOB, DONE]
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
                    self.currentState = C
                else:
                    if self.currentState == C and "done" in self.inputEvents and self.q == 0:
                        self.currentState = A
                    else:
                        if self.currentState == C and "done" in self.inputEvents and self.q > 0:
                            self.currentState = B
                        else:
                            if self.currentState == C and "job" in self.inputEvents and self.q > 0:
                                self.q += 1
                                self.currentState = C

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
            return {"req": True}  # Reformat
