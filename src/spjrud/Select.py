from src.expressions.Relation import Relation


class Select(Relation):
    # SELECT DISTINCT * FROM table
    # SELECT DISTINCT * FROM table WHERE a = b
    # table is a relation, a is an attribute and b is a const or an attribute
    def __init__(self, relation, op):
        super().__init__(None, relation.db_name, relation.schema)
        self.relation = relation
        self.op = op

    """
    The query follows the pattern:
    SELECT DISTINCT * FROM relation WHERE a [<,>,=,...] b
    """
    def get_query(self, conn):
        query = '(SELECT DISTINCT * FROM ' + self.relation.get_query(conn)
        query += f' WHERE {self.op})'
        return query

    """
    The query is valid if:
    - the sub query is valid
    - the attribute(s) is/are in the sub relation
    - the data type in the comparison matches
    """
    def is_valid(self):
        if not self.relation.is_valid():
            return False
        if not self.relation.has_attribute(self.op.get_a()):
            print(f'ERROR(Select): Attribute {self.op.get_a()} is not in relation')
        # when b is an attribute check if in relation
        if self.op.is_b_attribute():
            if not self.relation.has_attribute(self.op.get_b()):
                print(f'ERROR(Select): Attribute {self.op.get_b()} is not in relation')

        if not self.op.is_valid():
            print(f'ERROR(Select): Datatype between attributes do not match: {self.op}')
            return False

        return True
