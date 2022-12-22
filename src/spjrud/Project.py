from src.expressions.Relation import Relation


class Project(Relation):
    # SELECT DISTINCT a,b,... FROM table
    # table is a relation and a,b,... are attributes
    def __init__(self, relation, attributes):
        super().__init__(None, relation.db_name, attributes)
        self.relation = relation
        self.attributes = attributes

    """
    The query follows this pattern:
    SELECT DISTINCT attr_a, attr_b, ... FROM relation
    """
    def get_query(self, conn):
        query = '(SELECT DISTINCT'
        for attr in self.attributes:
            query += f' {attr},'
        # remove the last comma
        query = query[:len(query) - 1]
        query += f' FROM {self.relation.get_query(conn)})'

        return query
    """
    The query is valid if: 
    -the sub relation is valid
    -there is at least one attribute to project
    -all attributes provided are in the sub relation
    """
    def is_valid(self):
        if not self.relation.is_valid():
            return False

        if len(self.attributes) == 0:
            print('ERROR(Project): You need to provide attributes')
            return False
        # checks that every attr is in the relation
        for attribute in self.attributes:
            if not self.relation.has_attribute(attribute):
                print(f'ERROR(Project): The attribute ({attribute.name}, {attribute.data_type}) is not in the relation')
                return False

        return True
