# write a python program for search an element using linear search ;
n=int(input('enter number of elements you want : '))
a=[n]
print('enter elements : ')

for i in range(0,n):
    n1=int(input())
    a.append(n1)
key=int(input('enter element to search : '))
l=len(a)
loc=-1
for i in range(0,l-1):
    if key==a[i]:        
        loc=i
        break
if loc>=0:
    print('element is found at location : %i'%loc)
else:
    print('element does not exist !! ')
