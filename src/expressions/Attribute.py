class Attribute:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name
