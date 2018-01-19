class TestClass:
    className = "TestClass"
    def __init__(self,name):
        self.name = name
    def __add__(self,other):
        return self.name + " + " + other.name
    def __iadd__(self,other):
        self.name = self.name + ":" + other.name
        return self
    def __lt__(self,other):
        if len(self.name) < len(other.name):
            return True
        else:
            return False
    def __eq__(self,other):
        if self.name.upper() == other.name.upper():
            return True
        else:
            return False
    def __bool__ (self):
        if self.name == "Torsten:Ming":
            return True
        else:
            return False
    def __str__(self):
        return self.className + ":" + self.name

    def print(self):
        print(self.name)