import sqlite3

from src.expressions.Attribute import Attribute
from src.expressions.Relation import Relation
from src.expressions.Operation import Operation as Op

from src.spjrud.Select import Select
from src.spjrud.Project import Project
from src.spjrud.Join import Join
from src.spjrud.Rename import Rename
from src.spjrud.Union import Union
from src.spjrud.Difference import Difference


def pretty_print(sql_query, schema, algebra_result):
    print(sql_query + '\n')
    table = [schema] + algebra_result
    max_length = [0] * len(schema)
    for row in table:
        for col, cell in enumerate(row):
            if len(str(cell)) > max_length[col]:
                max_length[col] = len(str(cell))

    for i, row in enumerate(table):
        row_string = ''
        for col, cell in enumerate(row):
            row_string += str(cell) + (max_length[col] - len(str(cell))) * ' '
            row_string += '|'
        print(row_string)
        if i == 0:
            print('-' * len(row_string))

    print('\n')


"""
Print and returns the result of the provided algebra query, it can also save them as a new table in the database
:param db_name Database filename
:param algebra_query Relation object
:param save When set on true, the query result will be stored in the database
:param name Name of the new table must be provided when save is set to true
"""

def run(db_name, algebra_query, save=False, name=''):
    if save and name == '':
        print('If you wanna save the results you must provide a name for the table')
        return
    elif save and not name[0].isalpha():
        print('Your table name must start with a letter')
        return

    if algebra_query.is_valid():
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            res = algebra_query.get_query_result(cursor, save, name)
            if save:
                print('Your table is saved as ' + name)
            pretty_print(algebra_query.get_query(cursor), algebra_query.schema, res)
        return res


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

    # R
    a = Attribute('A', Attribute.INTEGER)
    b = Attribute('B', Attribute.INTEGER)
    c = Attribute('C', Attribute.INTEGER)

    r_table = Relation('R', DB, [a, b, c])

    # s
    d = Attribute('D', Attribute.INTEGER)
    b = Attribute('B', Attribute.INTEGER)
    c = Attribute('C', Attribute.INTEGER)

    s_table = Relation('S', DB, [b, c, d])

    queries = [
        Select(employees, Op(pay, Op.EQUAL, 50000)),
        Project(employees, [pay, last]),
        Join(r_table, s_table),
        Rename(departments, employee_nb, 'employee_count'),
        Union(employees, contractors),
        Difference(employees, contractors)
    ]
    for query in queries:
        if query.is_valid():
            get_result(DB, query)

        else:
            print('AYAYAYAYAYAYAYAYAYAYAYAYAYAYAYAYAAYAYAYAYAYAYAYAYAYA')
