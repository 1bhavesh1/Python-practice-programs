n1=0
n2=1
n3=0;
n=int(input('enter number upto you want to print series :'));
print(n1)
print(n2)
for i in range(n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    
