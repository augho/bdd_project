from src.spjrud.Connection import Connection


class Select(Connection):
    # SELECT DISTINCT * FROM table
    # SELECT DISTINCT * FROM table WHERE a = b
    # table is a relation, a is an attribute and b is a const or an attribute
    def __init__(self, relation, op):
        super().__init__()
        self.relation = relation
        self.op = op
        self.query = 'SELECT DISTINCT * FROM ' + relation.name
        self.query += f' WHERE {op.get_a()} {op.operation} {op.get_b()}'

    def __str__(self):
        pass
