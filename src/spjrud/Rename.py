from src.expressions.Relation import Relation
from src.expressions.Attribute import Attribute
import sqlite3
import uuid


class Rename(Relation):
    # ALTER TABLE table RENAME COLUMN curr_name TO new_name
    # table is a relation, curr_name is an attribute, new_name is a cst
    def __init__(self, relation, attribute_to_change, new_name):
        schema = []
        for attribute in relation.schema:
            if attribute.name == attribute_to_change.name:
                schema.append(Attribute(new_name, attribute.data_type))
            else:
                schema.append(Attribute(attribute.name, attribute.data_type))

        super().__init__(None, relation.db_name, schema)
        self.relation = relation
        self.attribute_to_change = attribute_to_change
        self.new_name = new_name
        self.table_name = None
    """
    In order to rename the attribute another temporary table is created and its column is renamed
    the query associated is then simply: SELECT * FROM new_table
    """
    def get_query(self, conn):
        if self.table_name is not None:
            return f'(SELECT * FROM {self.table_name})'

        table_name = 'rename_' + uuid.uuid4().hex
        self.table_name = table_name

        conn.execute(
            f'CREATE TEMPORARY TABLE {table_name} AS SELECT * FROM {self.relation.get_query(conn)};'
        )
        conn.execute(
            f'ALTER TABLE {table_name} RENAME COLUMN {self.attribute_to_change.name} TO {self.new_name};'
        )
        return f'(SELECT * FROM {table_name})'

    """
    The query is valid if:
    -the sub relation is valid
    -the sub relation contains the attribute to be renamed
    """
    def is_valid(self):
        if not self.relation.is_valid():
            return False
        if not self.relation.has_attribute(self.attribute_to_change):
            print(
                f'ERROR(Project): The attribute ({self.attribute_to_change.name},{self.attribute_to_change.data_type}) \
                 is not in the relation'
            )
            return False

        return True
