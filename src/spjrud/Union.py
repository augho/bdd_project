from src.expressions.Relation import Relation


class Union(Relation):
    # (SELECT * FROM table1) UNION (SELECT * FROM table2)
    # table1 and 2 are relations
    # need to make sure that columns have the same name
    def __init__(self, rel_a, rel_b):
        assert rel_a.db_name == rel_b.db_name

        super().__init__(None, rel_a.db_name, rel_a.schema)
        self.rel_a = rel_a
        self.rel_b = rel_b
    """
    The query follows the pattern:
    (SELECT * FROM rel_a) UNION (SELECT * FROM rel_b)
    """
    def get_query(self, conn):
        return f'(SELECT * FROM {self.rel_a.get_query(conn)} UNION SELECT * FROM {self.rel_b.get_query(conn)})'

    """
    The query is valid if:
    - Both sub queries are valid
    - The sub relations have the same attributes (in the same order too)
    """
    def is_valid(self):
        if not self.rel_a.is_valid() and self.rel_b.is_valid():
            return False

        if not len(self.rel_a.schema) == len(self.rel_b.schema):
            print('ERROR(Union||Difference): Relations must have the same nb of attributes')
            return False

        for count, attribute_a in enumerate(self.rel_a.schema):
            if attribute_a != self.rel_b.schema[count]:
                print('ERROR(Union||Difference): Relations attributes name or data_type do not match')
                return False

        return True
