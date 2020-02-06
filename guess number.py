# write a program to guess the number using random

import random

n=random.randint(1,100)

while True:
    print('guess a number between 1 to 100 : ')
    n1 = int(input())
    if n1 == n:
        print('yeah!!..you have guessed the number !')
        break
    elif n1<n:
        print('Try to guess a higher number... ! ')
    elif n1>n:
        print('Try to guess a lower number... !')
        
