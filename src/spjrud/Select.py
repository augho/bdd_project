from src.expressions.Relation import Relation


class Select(Relation):
    # SELECT DISTINCT * FROM table
    # SELECT DISTINCT * FROM table WHERE a = b
    # table is a relation, a is an attribute and b is a const or an attribute
    def __init__(self, relation, op):
        super().__init__(None, relation.db_name)
        self.relation = relation
        self.op = op

    def get_query(self, conn):
        query = '(SELECT DISTINCT * FROM ' + self.relation.get_query(conn)
        query += f' WHERE {self.op.get_a()} {self.op.operation} {self.op.get_b()})'
        return query
