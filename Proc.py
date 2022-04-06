class Proc:

    def __init__(self, name):
        self.currentState = None
        self.name = name

    def init(self):
        self.currentState = 0
        
    def internal(self):
        if self.currentState == 1:
            self.currentState = 0
            
        
