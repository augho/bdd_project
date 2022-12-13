from src.expressions.Relation import Relation


class Project(Relation):
    # SELECT DISTINCT a,b,... FROM table
    # table is a relation and a,b,... are attributes
    def __init__(self, relation, attributes):
        super().__init__(None, relation.db_name)
        self.relation = relation
        self.attributes = attributes

    def get_query(self, conn):
        query = '(SELECT DISTINCT'
        for attr in self.attributes:
            query += f' {attr},'
        # remove the last comma
        query = query[:len(query) - 1]
        query += f' FROM {self.relation.get_query(conn)})'

        return query
