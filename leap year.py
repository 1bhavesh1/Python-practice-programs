# write a program to find year is leap year or not using list and random number ;

import random

def leap():
    n=int(input('enter number of years in a list : '))
    a=[n]
    print('enter years in the list : ')

    for i in range(0,n):
        e1=int(input())
        a.append(e1)
        
    print('years in the list are : \n')
    print(a)
    print('\nchoosing a random year from a list .......\n')
    y=random.choice(a)

    while y>10:
        
        if y%4==0:
            print("\nyear {0} is a leap year ! ".format(y))
            break
        else:
            print("\nyear {0} is not a leap year !!".format(y))
            break
leap()
