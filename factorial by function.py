def fact():
    n=int(input('enter a number : '));
    f=1
    i=1
    while i<=n:
        f=f*i
        i+=1
    f=str(f)    
    print('factorial of number is : '+f)
fact()
        
