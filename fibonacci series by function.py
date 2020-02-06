#1. write a fibonacci funtion for n number ;
def fib():
    n1=0
    n2=1
    n=int(input('enter a number: '))
    print('fibonacci series is : %i'%n1)
    print(n2)
    for i in range(1,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
fib()
