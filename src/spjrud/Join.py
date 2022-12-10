from src.expressions.Relation import Relation


class Join(Relation):

    def __init__(self, rel_a, rel_b):
        super().__init__()
        self.subquery.append(rel_a)
        self.subquery.append(rel_b)
        self.query = f'SELECT * FROM {rel_a.name}, {rel_b.name}'
