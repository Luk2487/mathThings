# Maths Things

Python project with maths algorithms. Aims to understand how does machines compute these maths things. As of right now, it only contains a sequence module, where you can define a sequence as an object, and even put sequences into sequences. You can then calculate indexs.

## Expression Objects
There are used to store expressions such as $7x+2y$
```python
my_expression = Expression('7*x+2*y', 'x', 'y')
```

The first argument is the expression string, then there are the variables used in.
```python
a = 7*1+2*1
# an expression string is valid whenever replacing all of the variables with numbers is a valid operation
>>> 9 
```
Using the built-in functions, you can replace variables with values and then compute the expression

## Sequence Objects
Let's take an exemple:
let, for $n \in \mathbb{N}$, $u_{n+2} = u_{n+1} + u_n + n$ with $u_0 = 1$ and $u_1 = 1$

Let's create this sequence with a Sequence Object:
```python
variable = Sequence('un', 'n', 0)
variable.define_by_recursion(2, Expression('un_1 + un + n', 'un_1', 'un', 'n'), (1, 1))
```
`'un'` is the name of the sequence in the Expression Object, that is to say, how $u_n$ is translated. Following that, $u_{n+1}$ will translate into `'un_1'`.
If you call it `'some_random_name_lmao'`, then $u_{n+1}$ would be `'some_random_name_lmao_1'`. Defaults to `'un'`

`'n'` is the name of the variable in the Expression Object, (for $u_n$, the variable is $n$). Defaults to `'n'`

The third argument is the inferior born of the domain of definition of the sequence. $(u_n) \in \mathbb{N}$ so the sequence starts with $u_0$ and so the third argument is `0`. Defaults to `0`. 

Then come the **definition step** :
```python
def define_explicitly(expression_object: Expression):
  ...
def define_by_recursion(defined_at_n_plus: int, expression_object: Expression, first_terms: list | tuple):
  ...
```

$u_{n+2} = u_{n+1} + u_n$, with $u_0 = 0$ and $u_1 = 1$, the fibonacci sequence, would translate into
```python
Sequence('Fn').define_by_recursion(2, Expression('Fn_1 + Fn', 'Fn_1', 'Fn'), (0, 1))
```

Now you can use `.compute` and `.compute_in_list` to get the result.

Also, you can **integrate sequences in others** with `.include_sequence(var_in_expression, concerned_sequence, at_wich_index)`

```python
a = Sequence()
b = Sequence()
a.define_by_recursion(1, Expression('un + v', 'un', 'vn'), [1])
a.include_sequence('v', b, '2n + 3') # Note that you can't put sequences in the index.
```

This is the equivalent to $a_{n+1} = a_n + b_{2n+3}$ ($a_{n+1} = a_n + v$ and $v = b_{2n+3}$)

## To Be Continued
