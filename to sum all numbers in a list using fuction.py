def sum():
    a=[];
    i=0
    n=int(input('enter how many numbers you want in your list :'));
    for i in range(n):
        z=input('enter number :');
        a.append(z);
        a[i]=int(a[i])
    print('current list items :')
    print(a)
    s=0
    for x in a:
        s+=x
    s=str(s)
    print('sum of all numbers of list is : '+s)     
sum()
