class Project:
    # SELECT DISTINCT a,b,... FROM table
    # table is a relation and a,b,... are attributes
    def __init__(self, expr, attributes):
        self.expr = expr
        self.attributes = attributes

        self.query = 'SELECT DISTINCT'
        for attr in attributes:
            self.query += f' {attr},'
        # remove the last comma
        self.query = self.query[:len(self.query) - 1]
        self.query += f' FROM {expr.name}'

    def __str__(self):
        pass

    def apply(self, bdd):
        pass
