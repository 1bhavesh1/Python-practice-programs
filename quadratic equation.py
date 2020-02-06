# write a program to solve a quadratic equation

import cmath

a = float(input('enter value of a : '))
b = float(input('enter value of b : '))
c = float(input('enter value of c : '))

d = (b**2)-(4*a*c)

s1 = ((-b-cmath.sqrt(d))/(2*a))
s2 = ((-b+cmath.sqrt(d))/(2*a))

print('The solutions of equation are {0} and {1}'.format(s1,s2))
