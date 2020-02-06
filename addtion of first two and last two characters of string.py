a=input('enter a strning : ')
l=len(a)
if l>=2:
    f=a[0]+a[1]
    last=a[l-2]+a[l-1]
    sum=f+last
    print('the resultant string is : '+sum)
else:
    print('empty string')
    
