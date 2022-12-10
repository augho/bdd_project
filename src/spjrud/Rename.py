from src.expressions.Relation import Relation
import sqlite3


class Rename(Relation):
    # ALTER TABLE table RENAME COLUMN curr_name TO new_name
    # table is a relation, curr_name is an attribute, new_name is a cst
    def __init__(self, relation, curr_name, new_name):
        super().__init__()
        self.subquery.append(relation)
        self.curr_name = curr_name
        self.new_name = new_name

        self.query = f'SELECT DISTINCT * FROM {relation.name}'

    def _create_view(self, db_name):
        super()._create_view(db_name)
        with sqlite3.connect(db_name) as conn:
            query = 'ALTER VIEW {self.name} RENAME COLUMN {curr_name} TO {new_name}'
            print(query + ';')
            conn.execute(query + ';')

