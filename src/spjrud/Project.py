from src.spjrud.Connection import Connection


class Project(Connection):
    # SELECT DISTINCT a,b,... FROM table
    # table is a relation and a,b,... are attributes
    def __init__(self, relation, attributes):
        super().__init__()
        self.relation = relation
        self.attributes = attributes

        self.query = 'SELECT DISTINCT'
        for attr in attributes:
            self.query += f' {attr},'
        # remove the last comma
        self.query = self.query[:len(self.query) - 1]
        self.query += f' FROM {relation.name}'

    def __str__(self):
        pass
