from src.expressions.Relation import Relation


class Join(Relation):

    def __init__(self, rel_a, rel_b):
        assert rel_a.db_name == rel_b.db_name
        super().__init__(None, rel_a.db_name, rel_b.schema + rel_a.schema)
        # TODO change above line
        self.rel_a = rel_a
        self.rel_b = rel_b

    def get_query(self, conn):
        return f'(SELECT * FROM {self.rel_a.get_query(conn)}, {self.rel_b.get_query(conn)})'
