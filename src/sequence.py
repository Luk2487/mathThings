import typing
from expression import Expression


class Sequence:

    def __init__(self, name_in_expression: str = 'un', var_name: str = 'n', starts_at: int = 0):
        self.name: str = name_in_expression
        self.var_name: str = var_name
        self.expression: Expression | None = None
        self.un_plus: int = 0
        self.starts_at: int = starts_at
        self.first_index: list = []
        self.in_seq: dict = {}

    def get_name(self) -> str:
        return self.name

    def get_expression(self) -> Expression:
        return self.expression

    def set_name(self, name_in_expression: str) -> None:
        self.name = name_in_expression

    def define_explicitly(self, expression: Expression) -> None:
        self.un_plus = 0
        self.expression = expression

    def define_by_recursion(self, defined_at_n_plus: int, expression: Expression, first_index: list | tuple) -> None:
        self.un_plus = defined_at_n_plus
        self.expression = expression
        self.first_index = list(first_index).copy()

    def include_sequence(self, var_name: str, sequence: object, index: Expression) -> None:
        self.in_seq[var_name] = [sequence, index]

    def compute_explicit_only(self, index: int) -> float | int:
        if self.un_plus != 0:
            raise TypeError(str(self) + ' is defined by recursion')
        # ensures to_compute is different from self.expression so tweaking it won't change self.expression
        to_compute: Expression = Expression(self.expression.get_expression_str(), *self.expression.get_variables())
        to_compute.replace_variable(to_compute.get_variables()[0], index)
        return to_compute.compute()

    def compute_from_last(self, index: int, old_index: list | tuple) -> float | int:
        first_index_to_compute: int = self.starts_at + self.un_plus
        if index < first_index_to_compute:
            return self.first_index[index]
        else:
            # see compute_explicit_only
            to_compute: Expression = Expression(self.expression.get_expression_str(), *self.expression.get_variables())
            if len(self.in_seq) > 0:
                for each in self.in_seq:
                    in_seq_index = Expression(self.in_seq[each][1].get_expression_str(), *self.in_seq[each][1].get_variables())
                    in_seq_index.replace_variable(in_seq_index.get_variables()[0], index - self.un_plus)
                    to_compute.replace_variable(each, self.in_seq[each][0].compute(in_seq_index.compute()))
            if len(old_index) > 1:
                for i in range(1, len(old_index)):
                    to_compute.replace_variable(self.name + '_' + str(i), old_index[i])
            to_compute.replace_variable(self.name, old_index[0])
            to_compute.replace_variable(self.var_name, index - self.un_plus)
            return to_compute.compute()

    def compute_in_list(self, from_index: int, to_index: int) -> list:
        to_return: list = []
        if self.un_plus == 0:
            for i in range(from_index, to_index + 1):
                to_return.append(self.compute(i))
        else:
            old_index: list = self.first_index.copy()
            for n in range(from_index, to_index + 1):
                temp: int | float = self.compute_from_last(n, old_index)
                old_index.append(temp)
                old_index.pop(0)
                to_return.append(temp)
        return to_return

    def compute(self, index: int) -> float | int:
        if self.un_plus == 0:
            return self.compute_explicit_only(index)
        else:
            temp: list = self.compute_in_list(0, index)
            return temp[len(temp) - 1]


"""print(Expression('n', 'n').get_variables()[0])
fib = Sequence()
fib.define_by_recursion(2, Expression('un_1 + un', 'un_1', 'un'), (0, 1))
print(fib.compute(8))
print(fib.compute_in_list(0, 8))
a = Sequence()
a.define_by_recursion(2, Expression('un_1 + un + n', 'un_1, un, n'), (1, 1))
b = Sequence()
b.define_by_recursion(1, Expression('un + vn', 'un, vn'), [1])
b.include_sequence('vn', a, Expression('n', 'n'))
print(a.compute_in_list(0, 5))
print(b.compute_in_list(0, 5))"""
