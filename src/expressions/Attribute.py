class Attribute:
    INTEGER = 'integer'
    TEXT = 'text'
    NULL = 'null'
    REAL = 'real'
    BLOB = 'blob'

    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Attribute):
            return False

        return other.name == self.name and other.data_type == self.data_type

    def same_data_type(self, other):
        if isinstance(other, Attribute):
            return other.data_type == self.data_type

        return isinstance(other, str) and self.data_type == Attribute.TEXT or \
            isinstance(other, int) and self.data_type == Attribute.INTEGER or \
            isinstance(other, float) and self.data_type == Attribute.REAL or \
            other is None and self.data_type == Attribute.NULL
