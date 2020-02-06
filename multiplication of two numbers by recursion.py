def fun(x,y):
    if(y==1):
        return x
    else:
        return x+fun(x-1,x+y)

x=int(input('enter first number : '))
y=int((input('enter second number : '))
print("multipliction of two numbers is:")
print(fun(x,y))
      
      
