# write program for addding two list elements and store in third list

n=int(input('enter number of elements in lists : '))
first=[n]
print('enter elements of first list : ')
for i in range(n):
    e1=int(input())
    first.append(e1)
second=[n]
print('enter elements of second list : ')
for i in range(n):
    e2=int(input())
    second.append(e2)
third=[]
for i in range(0,len(first)):
    third.append(first[i]+second[i])
print('after addition elements in third list will be : ')
for ele in third:
    print(ele , end=" ")

    
