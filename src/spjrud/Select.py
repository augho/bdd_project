class Select:
    # SELECT DISTINCT * FROM table
    # SELECT DISTINCT * FROM table WHERE a = b
    # table is a relation, a is an attribute and b is a const or an attribute
    def __init__(self, relation, a, b):
        self.relation = relation
        self.a = a
        self.b = b

    def __str__(self):
        pass

    def apply(self, relation):
        pass
