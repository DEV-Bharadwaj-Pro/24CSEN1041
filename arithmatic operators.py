a = 9
b = 5
c="Hello"
d="World"

# Arithmetic Operators
print(f"Arithmatic operators")
print(f"{a} + {b} = {a + b}")
print("{a} - {b} = {a - b}") 
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.5f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}")
print(f"{c} + {d} = {c + d}")
print(f"{c} - {d} = {c - d}") 

'''Arithmatic operators
9 + 5 = 14
{a} - {b} = {a - b}
9 * 5 = 45
9 / 5 = 1.80000
9 % 5 = 4
Hello + World = HelloWorld
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 14, in <module>
  TypeError: unsupported operand type(s) for -: 'str' and 'str'''

