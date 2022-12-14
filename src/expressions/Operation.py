from src.expressions.Attribute import Attribute


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
        return self._a

    def get_b(self):
        return self._b

    def is_b_attribute(self):
        return isinstance(self._b, Attribute)

    def is_valid(self):
        return self._a.same_data_type(self._b)

