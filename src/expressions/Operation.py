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

    """
    :return True when a and b have the same data type
    """
    def is_valid(self):
        return self._a.same_data_type(self._b)

    def __str__(self):
        return f'{self.get_a()} {self.operation} {self.get_b()}'

