from src.expressions.Attribute import Attribute
from src.expressions.Relation import Relation
from src.expressions.Operation import Operation as Op

from src.spjrud.Select import Select
from src.spjrud.Project import Project
from src.spjrud.Join import Join
from src.spjrud.Rename import Rename
from src.spjrud.Union import Union
from src.spjrud.Difference import Difference


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


def pretty_print(query_result, attributes=None):
    pass


def get_result(db_name, algebra_query):
    with sqlite3.connect(db_name) as conn:
        res = algebra_query.get_query_result(conn)

    print(res)
    return res


def testing():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        query1 = "PRAGMA table_info(employees);"
        query2 = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(query1)
        print(cursor.fetchall())


def lazy_unit_test():
    DB = 'test.db'

    # employees
    pay = Attribute('pay', Attribute.INTEGER)
    first = Attribute('first', Attribute.TEXT)
    last = Attribute('last', Attribute.TEXT)

    employees = Relation('employees', DB, [first, last, pay])

    # departments
    name = Attribute('name', Attribute.TEXT)
    budget = Attribute('budget', Attribute.INTEGER)
    employee_nb = Attribute('employee_nb', Attribute.INTEGER)
    chief = Attribute('chief', Attribute.TEXT)

    departments = Relation('departments', DB, [name, budget, employee_nb, chief])

    # contractors
    contractors = Relation('contractors', DB, [first, last, pay])

    employee_count = Attribute('employee_count', Attribute.INTEGER)

    queries = [
        Select(employees, Op(pay, Op.EQUAL, 50000)),
        Project(employees, [pay, last]),
        Join(employees, departments),
        Rename(departments, employee_nb, 'employee_count'),
        Union(employees, contractors),
        Difference(employees, contractors)
    ]
    for query in queries:
        get_result(DB, query)


if __name__ == '__main__':
    DB = 'test.db'

    # employees
    pay = Attribute('pay', Attribute.INTEGER)
    first = Attribute('first', Attribute.TEXT)
    last = Attribute('last', Attribute.TEXT)

    employees = Relation('employees', DB, [first, last, pay])

    # departments
    name = Attribute('name', Attribute.TEXT)
    budget = Attribute('budget', Attribute.INTEGER)
    employee_nb = Attribute('employee_nb', Attribute.INTEGER)
    chief = Attribute('chief', Attribute.TEXT)

    departments = Relation('departments', DB, [name, budget, employee_nb, chief])

    # contractors
    contractors = Relation('contractors', DB, [first, last, pay])

    employee_count = Attribute('employee_count', Attribute.INTEGER)

    s = Select(employees, Op(pay, Op.EQUAL, 50000))
    p = Project(employees, [pay, last])
    j = Join(employees, departments)
    r = Rename(departments, employee_nb, 'employee_count')
    u = Union(employees, contractors)
    d = Difference(employees, contractors)

    # get_result(DB, s)
    lazy_unit_test()








