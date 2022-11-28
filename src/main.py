from src.expressions.Attribute import Attribute
from src.expressions.Relation import Relation
from src.expressions.Operation import Operation as Op

from src.spjrud.Select import Select
from src.spjrud.Project import Project
from src.spjrud.Union import Union
from src.spjrud.Connection import Connection

import sqlite3

# informatique.umons.ac.be/ssi/

TABLE = \
    'CREATE TABLE COMPANY' + \
    '(ID     INT     PRIMARY KEY     NOT NULL,' + \
    'NAME    TEXT    NOT NULL,' + \
    'AGE     INT     NOT NULL,' + \
    'ADDRESS CHAR' + \
    'SALARY  REAL);'

"""CREATE TABLE contractors (
    first text,
    last text,
    pay integer
);
"""


if __name__ == '__main__':
    DB = 'test.db'
    employees = Relation('employees')
    departments = Relation('departments')
    contractors = Relation('contractors')

    pay = Attribute('pay', 10000)
    first = Attribute('first', 'Karen')
    last = Attribute('last', 'Pils')

    s = Select(employees, Op(pay, Op.EQUAL, 50000))
    p = Project(employees, [pay, last])
    u = Union(employees, contractors)

    print(u.get('test.db'))







