import sqlite3


class Relation:
    def __init__(self, name, db_name, schema):
        self.name = name
        self.db_name = db_name
        self.schema = schema

    """
    :param cursor connection to the db
    :return Results of the query of this relation
    """
    def get_query_result(self, cursor, save, name):
        query = f'SELECT DISTINCT * FROM {self.get_query(cursor)};'
        res = cursor.execute(query).fetchall()
        if save:
            query = f'CREATE TABLE {name} AS {query}'
            cursor.execute(query)

        return res

    """
    Assert that the relation has at least one attribute
    """
    def is_valid(self):
        if len(self.schema) > 0:
            return True
        print(f'Relation {self.name} has no attribute')
        return False

    def get_query(self, conn):
        return self.name

    def has_attribute(self, attribute):
        for attr in self.schema:
            if attr == attribute:
                return True

        return False

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
