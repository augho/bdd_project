class Operation:
    EQUAL = '='
    GT = '>'
    LT = '<'
    GTE = '>='
    LTE = '<='
    D = '!='

    def __init__(self, a, operation, b):
        self._a = a
        self.operation = operation
        self._b = b

    def get_a(self):
        return str(self._a)

    def get_b(self):
        return str(self._b)
