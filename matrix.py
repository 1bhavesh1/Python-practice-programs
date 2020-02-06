# write a prorgam to define a matrix and print it

a=[]
n=int(input('enter N for N x N matrix : '))
print('enter elements : ')
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print('Display array in matrix form : ')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
