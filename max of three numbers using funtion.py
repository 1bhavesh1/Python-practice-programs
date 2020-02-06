def max():
    print('enter three numbers :')
    n1=int(input());
    n2=int(input());
    n3=int(input());
    if n1>n2 and n1>n3:
        n1=str(n1)
        print(n1+' is maximum among three')
    elif n2>n3 and n2>n1:
         n2=str(n2)
         print(n2+' is maximum among three')
    else:
         n3=str(n3)
         print(n3+' is maximum among three')
max()         
