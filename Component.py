from abc import ABC, abstractmethod

from Const.Const import JOB, DONE, REQ


class Component(ABC):
    def __init__(self, name):
        self.name = name
        self.inputEvents = {}  # Notify by other components
        self.inputs = []
        self.outputEvents = {}
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

    @abstractmethod
    def conflict(self):
        pass

    def write(self, key, value):  # Write event and notify all entry
        outputEvents = {key: value}
        self.outputEvents.update(outputEvents)

    def deleteEvent(self, key):
        del self.inputEvents[key]
