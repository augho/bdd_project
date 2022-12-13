from src.expressions.Relation import Relation
import sqlite3
import uuid


class Rename(Relation):
    # ALTER TABLE table RENAME COLUMN curr_name TO new_name
    # table is a relation, curr_name is an attribute, new_name is a cst
    def __init__(self, relation, curr_name, new_name):
        super().__init__(None, relation.db_name)
        self.relation = relation
        self.curr_name = curr_name
        self.new_name = new_name
        self.table_name = None

    def get_query(self, conn):
        if self.table_name is not None:
            return f'(SELECT * FROM {self.table_name})'

        table_name = 'rename_' + uuid.uuid4().hex
        self.table_name = table_name

        conn.execute(
            f'CREATE TEMPORARY TABLE {table_name} AS SELECT * FROM {self.relation.get_query(conn)};'
        )
        conn.execute(
            f'ALTER TABLE {table_name} RENAME COLUMN {self.curr_name} TO {self.new_name};'
        )
        return f'(SELECT * FROM {table_name})'

