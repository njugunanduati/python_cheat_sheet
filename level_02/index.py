"""
This level we will talk about variable
"""
# Variables
name = "James"
age = 38
salary = 150000
active = True

print(name)
print(age)
print(salary)
print(active)

# Python is dynamically typed
x = 10
print(f'Value of x is {x} which is a {type(x)}')
x = "hello"
print(f'Value of x is "{x}" which is a {type(x)}')
x = [1, 2, 3]
print(f'Value of x is {x} which is a {type(x)}')

# Multiple assigment
a, b = 10, 20
print("a", a)
print("b", b)

# Swap
a, b = b, a
print("a", a)
print("b", b)

# Same value
x = y = z = 0

# Delete
del x
