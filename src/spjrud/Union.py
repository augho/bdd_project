from src.expressions.Relation import Relation


class Union(Relation):
    # (SELECT * FROM table1) UNION (SELECT * FROM table2)
    # table1 and 2 are relations
    # need to make sure that columns have the same name
    def __init__(self, rel_a, rel_b):
        super().__init__()
        self.subquery.append(rel_a)
        self.subquery.append(rel_b)
        self.query = f'SELECT * FROM {rel_a.name} UNION SELECT * FROM {rel_b.name}'
