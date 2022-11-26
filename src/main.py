import sqlite3 as sql3

#http://informatique.umons.ac.be/ssi/

TABLE = \
    'CREATE TABLE COMPANY' + \
    '(ID     INT     PRIMARY KEY     NOT NULL,' + \
    'NAME    TEXT    NOT NULL,' + \
    'AGE     INT     NOT NULL,' + \
    'ADDRESS CHAR' + \
    'SALARY  REAL);'

"""CREATE TABLE employees (
    first text,
    last text,
    pay integer
);
"""
conn = sql3.connect('test.db')
c = conn.cursor()


def insert_emp(emp):
    with conn:
        c.execute(f"INSERT INTO employees VALUES ({emp.first}, {emp.last}, {emp.pay})")


def main():
    pass


c.execute("SELECT * FROM employees")

print(c.fetchall())

conn.commit()

conn.close()
