from abc import ABC, abstractmethod

from Const.Const import JOB, DONE, REQ


class Component(ABC):
    def __init__(self, name):
        self.name = name
        self.inputEvents = {}
        self.inputs = []
        self.currentState = None  # ToDo Remove after
        self.tr = 0
        self.te = 0
        self.tl = 0
        self.tn = 0

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def internal(self):
        pass

    @abstractmethod
    def external(self):
        pass

    @abstractmethod
    def avancement(self):
        pass

    @abstractmethod
    def generateOutput(self):
        pass

    def write(self, key, value):  # Write event and notify all entry
        outputEvents = {key: value}
        # Consulter les entrees connectees
        if key in self.inputs:
            self.inputEvents.update(outputEvents)

    def deleteEvent(self, key):
        del self.inputEvents[key]


class Connecteur:
    def __init__(self, G, B, F):
        self.G = G
        self.B = B
        self.F = F
