import sqlite3
import uuid


class Relation:
    def __init__(self, name=None):
        if name is not None:
            self.name = name
        else:
            self.name = uuid.uuid4().hex

        self.query = None
        self.subquery = []

    def set_subquery(self, subquery):
        self.subquery = subquery

    def get_query_result(self, db_name):
        self._create_view(db_name)

        with sqlite3.connect(db_name) as conn:
            res = conn.execute(f'SELECT DISTINCT * FROM {self.name};')

        return res.fetchall()

    def _create_view(self, db_name):
        # if query is none then it's a relation already in the db
        if self.query is None:
            return

        for subquery in self.subquery:
            subquery._create_view(db_name)
        with sqlite3.connect(db_name) as conn:
            query = f'CREATE VIEW {self.name} AS ' + self.query
            print(query + ';')
            conn.execute(query + ';')

    @staticmethod
    def insert(db_name, table, attributes):
        with sqlite3.connect(db_name) as conn:
            query = f'INSERT INTO {table.name} ('

            for attribute in attributes:
                query += attribute.name + ', '
            query = query[:len(query) - 2]
            query += ') VALUES('

            for attribute in attributes:
                query += '"' + str(attribute.value) + '", '
            query = query[:len(query) - 2]
            query += ');'

            cur = conn.cursor()
            print(query)
            cur.execute(query)
            conn.commit()

    def __str__(self):
        return self.name
