from math import inf

from Component import Component
from Const.Const import JOB, A, B, C, DONE, REQ


class Buf(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.inputs = [JOB, DONE]
        self.q = 0

    def init(self):
        self.currentState = A

    def internal(self):
        if self.currentState == B:
            self.q -= 1
            self.currentState = A
        print(f'current State: {self.currentState}')

    def external(self):
        # print(f'inputEvents{self.name}: {self.inputEvents}')
        if self.currentState == A and JOB in self.inputEvents:
            # print(f'{JOB} is in inputEvents')
            self.currentState = B
            self.q += 1
        elif self.currentState == C and "job" in self.inputEvents:
            self.q += 1
            self.currentState = C
        elif self.currentState == C and "done" in self.inputEvents and self.q == 0:
            self.currentState = A
        elif self.currentState == C and "done" in self.inputEvents and self.q > 0:
            self.currentState = B
        # self.inputEvents = {}
        print(f'current State: {self.currentState}')

    def avancement(self):
        if self.currentState == A:
            return inf
        elif self.currentState == B:
            return 0.0
        elif self.currentState == C:
            return inf
        return -1

    def generateOutput(self):
        if self.currentState == B:
            Component.write(self, REQ, True)
            print(f'q: {self.q}')
            print("Output generate REQ")
            return {"req": True}  # Reformat

    def conflict(self):
        self.internal()