from src.expressions.Attribute import Attribute
from src.expressions.Relation import Relation
from src.expressions.Operation import Operation as Op

from src.spjrud.Select import Select
from src.spjrud.Project import Project
from src.spjrud.Join import Join
from src.spjrud.Rename import Rename
from src.spjrud.Union import Union
from src.spjrud.Difference import Difference

from src.functions import lazy_unit_test, run

# informatique.umons.ac.be/ssi/


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

    s = Select(employees, Op(pay, Op.EQUAL, 50000))
    p = Project(employees, [pay, last])
    j = Join(employees, departments)
    r = Rename(departments, employee_nb, 'employee_count')
    u = Union(employees, contractors)
    d = Difference(employees, contractors)
    hard = Select(u, Op(pay, Op.EQUAL, 50000))
    hardBis = Select(u, Op(pay, Op.LT, 50000))

    run(DB, u, True, 'thisisatest')
    # lazy_unit_test()








