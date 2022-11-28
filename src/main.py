from src.expressions.Attribute import Attribute
from src.expressions.Relation import Relation
from src.expressions.Operation import Operation as Op

from src.spjrud.Select import Select
from src.spjrud.Project import Project
from src.spjrud.Connection import Connection

# informatique.umons.ac.be/ssi/

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


if __name__ == '__main__':
    table = Relation('employees')
    pay = Attribute('pay', 300000)
    first = Attribute('first', 'Michael B')
    last = Attribute('last', 'Jordan')

    #s = Select(table, Op(pay, Op.EQUAL, 50000))
    #p = Project(table, [pay, last])
    Connection().insert('test.db', table, [first, last, pay])
    #print(p.get('test.db'))







