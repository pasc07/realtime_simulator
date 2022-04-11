from math import inf

from Component import Component
from Const.Const import INIT, GEN_OUTPUT, STEP


class Adder(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        # self.nb_inputs = nb_inputs
        # self.nb_outputs = nb_outputs
        self.values = None
        self.previous_out = 0.0
        self.output = 0.0
        self.inputs = []
        self.temp_inputEvents = {}

    def init(self):
        self.currentState = INIT
        self.output = 0.0

    def internal(self):
        if self.currentState == GEN_OUTPUT:
            self.currentState = INIT
            print(f'Current state Adder : {self.currentState}')

    def external(self):
        if self.currentState == INIT and self.inputEvents:
            print(f'inputEvent Adder : {self.inputEvents}')
            self.temp_inputEvents.update(self.inputEvents)
            self.currentState = GEN_OUTPUT
            print(f'Current state Adder : {self.currentState}')

    def avancement(self):
        if self.currentState == INIT:
            return inf
        elif self.currentState == GEN_OUTPUT:
            return 0.0
        return -1

    def generateOutput(self):
        if self.currentState == GEN_OUTPUT:
            self.write("adder", self.add())
            print("Add operation occured")

    def conflict(self):
        self.external()

    def add(self):

        self.values = list(self.temp_inputEvents.values())
        print(f'+++++++ les values : {self.values}')
        add = 0
        self.previous_out = self.output
        for value in self.values:
            if value is not None:
                add += float(value)
            print(f'value: {float(value)} ')
        self.output = add
        print(f'output adder: {self.output}')
        return self.output
