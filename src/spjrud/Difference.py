class Difference:
    # (SELECT * FROM table1) MINUS (SELECT * FROM table2)
    # table1 and 2 are relations
    # need to make sure that columns have the same name
    def __init__(self, expr_a, expr_b):
        self.expr_a = expr_a
        self.expr_b = expr_b

    def __str__(self):
        pass
