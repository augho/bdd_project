class Rename:
    def __init__(self, expr, old_name, new_name):
        self.expr = expr
        self.old_name = old_name
        self.new_name = new_name

        self.query = ''

    def __str__(self):
        pass
