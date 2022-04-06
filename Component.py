from abc import ABC, abstractmethod

from Const.Const import JOB, DONE, REQ


class Component(ABC):
    def __init__(self, name):
        self.name = name
        self.inputEvents = {JOB: False, REQ: False, DONE: False}
        #self.inputs = []
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

    def write(self, key, value):
        self.inputEvents[key] = value

    def delete(self, key):
        del self.inputEvents[key]

    def updateInput(self, key):
        self.inputs = list(key)

    def inputEventWrapper(self):
        pass
