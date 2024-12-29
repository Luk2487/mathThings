import typing


class SequenceFuncOfN:

    def __init__(self, equation):
        self.equation: str = equation

    def compute_index(self, index: int) -> int:
        to_compute: str = self.equation.replace('n', str(index))
        to_return: int = eval(to_compute)
        return to_return


class SequenceByRecursion:
    # let name be un, so un+1 translate to un_1...  ex: fib = SequenceByRecursion('an', 2, 0, 'an_1+an', [1, 1])
    # first_index should contain, in order, u0, u1...
    def __init__(self, name: str, un_plus: int, start_at: int, equation: str, first_index: list[int]):
        self.equation: str = equation
        self.un_plus: int = un_plus
        self.name: str = name
        self.first_index: list[int] = first_index
        self.start_at: int = start_at
        self.included_sequences: dict = dict()

    def compute_index(self, index: int, return_all_as_list: bool) -> int | list[int]:
        values_list: list = []
        old_values: list[int] = self.first_index.copy()
        first_index_to_compute: int = self.start_at + self.un_plus
        if index >= first_index_to_compute:
            for n in range(first_index_to_compute, index + 1):
                new_equation: str = self.equation
                if len(self.included_sequences) > 0:
                    for each in self.included_sequences:
                        new_equation = replace_included_sequence(new_equation, n - self.un_plus, each, self.included_sequences[each][0], self.included_sequences[each][1])
                new_equation = replace_equation_with_values(self.name, new_equation, n, self.un_plus, old_values)
                to_return: int = compute_calcul(new_equation)
                values_list.append(to_return)
                old_values.pop(0)
                old_values.append(to_return)
        else:
            to_return: int = self.first_index[index]
        if return_all_as_list:
            return self.first_index + values_list
        else:
            return to_return

    def include_sequence(self, name: str, sequence: object, index: str) -> None:
        self.included_sequences[name] = (sequence, index)


def replace_n_with_value(equation: str, value: int) -> str:
    to_return: str = equation.replace('n', str(value))
    return to_return


def replace_un_with_value(equation: str, name: str, value: int) -> str:
    to_return: str = equation.replace(name, str(value))
    return to_return


def replace_equation_with_values(seq_name: str, equation: str, n: int, un_plus: int, old_values: list[int]) -> str:
    if seq_name in equation:
        if len(old_values) > 1:
            for i in range(1, len(old_values)):
                equation = replace_un_with_value(equation, seq_name + '_' + str(i), old_values[i])
        equation = replace_un_with_value(equation, seq_name, old_values[0])
    equation = replace_n_with_value(equation, n - un_plus)
    return equation


def compute_calcul(calcul: str) -> int:
    to_return: int = eval(calcul)
    return to_return


def replace_included_sequence(equation: str, n: int, var_name: str, sequence: object, index_equation: str) -> str:
    computed_index: int = compute_calcul(replace_n_with_value(index_equation, n))
    var_value: int = sequence.compute_index(computed_index)
    to_return: str = replace_un_with_value(equation, var_name, var_value)
    return to_return


fib = SequenceByRecursion('an', 2, 0, 'an_1 + an', [0, 1])
print(fib.compute_index(10, True))
