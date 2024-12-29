# Maths Things

Python project with maths algorithms. Aims to understand how does machines compute these maths things. As of right now, it only contains a sequence module, where you can define a sequence as an object, and even put sequences into sequences. You can then calculate indexs.

## Expression Objects
There are used to store expressions such as $7x+2y$

`my_expression = Expression('7*x+2*y', 'x', 'y')`

The first argument is the expression string, then there are the variables used in.
```
a = 7*1+2*1
# an expression string is valid whenever replacing all of the variables with numbers is a valid operation
>>> 9 
```
Using the built-in functions, you can replace variables with values and then compute it

## Sequence Objects
Let's take an exemple:
let, for $n \in \mathbb{N}$, $u_{n+2} = u_{n+1} + u_n + n$ with $u_0 = 1$ and $u_1 = 1$

Let's create this sequence with a Sequence Object:
```
variable = Sequence('un', 'n', 0)
variable.define_by_recursion(2, Expression('un_1 + un + n', 'un_1', 'un', 'n'), (1, 1))
```
`'un'` is the name of the sequence in the Expression Object, that is to say, how $u_n$ is translated. Following that, $u_{n+1}$ will translate into `'un_1'`.
If you call it `'some_random_name_lmao'`, then $u_{n+1}$ would be `'some_random_name_lmao_1'`. Defaults to `'un'`

`'n'` is the name of the variablein the Expression Object, for $u_n$, this is $n$. Defaults to `'n'`

The third argument is the inferior born of the domain of definition of the sequence. Defaults to `0`. $(un) \in \mathbb{N}$ so the sequence starts with $u_0$


