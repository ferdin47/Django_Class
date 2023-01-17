# https://www.geeksforgeeks.org/taking-input-in-python/
# https://www.programiz.com/python-programming/examples/quadratic-roots
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = int(input('enter a as 1 - ')) #1
b = int(input('enter b as 5 - ')) #5
c = int(input('enter c as 6 - ')) #6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))