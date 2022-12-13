import sqlite3


class Relation:
    def __init__(self, name, db_name):
        self.name = name
        self.db_name = db_name

    def get_query_result(self, conn):
        res = conn.execute(f'SELECT DISTINCT * FROM {self.get_query(conn)};')

        return res.fetchall()

    def get_query(self, conn):
        return self.name

    def _get_metadata(self):
        pass

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
