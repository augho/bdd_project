from src.expressions.Relation import Relation


class Union(Relation):
    # (SELECT * FROM table1) UNION (SELECT * FROM table2)
    # table1 and 2 are relations
    # need to make sure that columns have the same name
    def __init__(self, rel_a, rel_b):
        assert rel_a.db_name == rel_b.db_name
        super().__init__(None, rel_a.db_name)
        self.rel_a = rel_a
        self.rel_b = rel_b

    def get_query(self, conn):
        return f'(SELECT * FROM {self.rel_a.get_query(conn)} UNION SELECT * FROM {self.rel_b.get_query(conn)})'
