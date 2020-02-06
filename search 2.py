# write a program for binary search ;

def binsearch(a,low,high,key):
    if high>=1:
        mid = (low+high)/2
        mid=int(mid)
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            return binsearch(a,low,mid-1,key)
        else:
            return binsearch(a,mid+1,high,key)
    else:
        return -1

n=int(input('enter how many elements you want : '))
a=[n]
print('enter elements : ')
for i in range(0,n):
    n1=int(input())
    a.append(n1)
key=int(input('enter element to search for : '))
l=len(a)
result=binsearch(a,0,l-1,key)
if result != -1:
    print("element is found at location %d"%result)
else:
    print("element is not found !! ")
