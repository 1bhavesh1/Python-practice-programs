s=input('enter a string :')
str1=''
index=len(s)
while index>0:
    str1+=s[index-1]
    index=index-1
print('reverse of string is : '+str1)    
    
