from Component import Component
from Const.Const import INIT, GEN_OUTPUT


class Adder(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        # self.nb_inputs = nb_inputs
        # self.nb_outputs = nb_outputs
        self.output = 0.0

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
            self.currentState = GEN_OUTPUT
            print(f'Current state Adder : {self.currentState}')

    def avancement(self):
        pass

    def generateOutput(self):
        if self.currentState == GEN_OUTPUT:
            self.write("output", "add")
            print("Add operation")
        else:
            self.write("output", "No_operation")
            print("No operation")

    def conflict(self):
        self.external()
        self.internal()

    def add(self, dictionary):
        # Wrapper dict to list
        if self.outputEvents["output"] == "add":
            values = list(dictionary.values())
            add = 0
            for value in values:
                if value is not None:
                    add += float(value)
                print(f'value: {float(value)} ')
            self.output = add
            print(f'output adder: {add}')
            return self.output
