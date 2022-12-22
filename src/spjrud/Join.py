from src.expressions.Relation import Relation


class Join(Relation):

    def __init__(self, rel_a, rel_b):
        assert rel_a.db_name == rel_b.db_name
        self.rel_a = rel_a
        self.rel_b = rel_b

        # checks the common attributes between the relations
        schema = []
        self.common_attributes = []
        for attribute_a in rel_a.schema:
            for attribute_b in rel_b.schema:
                if attribute_a == attribute_b:
                    self.common_attributes.append(attribute_a)

        # construction of the result's schema:
        # {a's attributes - common attributes} + common attributes + {b's attributes - common attributes}
        for attribute_a in rel_a.schema:
            is_common = False
            for common_attr in self.common_attributes:
                if attribute_a == common_attr:
                    is_common = True

            if not is_common:
                schema.append(attribute_a)

        schema += self.common_attributes

        for attribute_b in rel_b.schema:
            is_common = False
            for common_attr in self.common_attributes:
                if attribute_b == common_attr:
                    is_common = True

            if not is_common:
                schema.append(attribute_b)

        super().__init__(None, rel_a.db_name, schema)

    """
    The query follows this pattern:
    SELECT * FROM rel_a JOIN rel_b USING (common_attribute1, common_attribute2, ...)
    """
    def get_query(self, cursor):
        query = f'(SELECT * FROM {self.rel_a.get_query(cursor)})'
        query += f'JOIN {self.rel_b.get_query(cursor)} USING('
        for attr in self.common_attributes:
            query += f' {attr},'
        # remove the last comma
        query = query[:len(query) - 1]

        return query + ')'

    """
    The query is valid if:
    - Both sub queries are valid
    """
    def is_valid(self):
        return self.rel_a.is_valid() and self.rel_b.is_valid()
