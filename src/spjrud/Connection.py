import sqlite3


class Connection:

    def __init__(self):
        self.query = None

    def get(self, db_name):
        with sqlite3.connect(db_name) as conn:
            print(self.query + ';')
            res = conn.execute(self.query + ';')

        return res.fetchall()

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
