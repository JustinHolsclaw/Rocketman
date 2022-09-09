class Body:
    def __init__(self, name, mass):
        self.name = name
        self.compatibleEngines = []
        self.currentEngine = self.compatibleEngines[0]
        self.mass = mass