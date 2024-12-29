import typing


class Expression:

    def __init__(self, expression_str: str, *variables: str):
        self.expression: str = expression_str
        self.variables: list = list(variables).copy()

    def get_expression_str(self) -> str:
        return self.expression

    def get_variables(self) -> list:
        return self.variables

    def set_expression_str(self, expression_str: str) -> None:
        self.expression = expression_str

    def set_variables(self, *variables: str) -> None:
        self.variables = list(variables)

    def append_variable(self, variable: str) -> None:
        self.variables.append(variable)

    def remove_variable(self, variable: str) -> None:
        self.variables.remove(variable)

    def replace_variable(self, variable: str, value: float | int) -> None:
        new_value: str = self.expression.replace(variable, str(value))
        self.expression = new_value

    def replace_all_variables(self, *values: float | int) -> None:
        if len(values) != len(self.variables):
            raise IndexError(str(*self.variables) + ' can\'t be replaced by ' + str(*values) + ', the length is different')
        for i in range(0, len(values)):
            self.replace_variable(self.variables[i], values[i])

    def compute(self) -> float | int:
        to_return: float | int = eval(self.expression)
        return to_return
