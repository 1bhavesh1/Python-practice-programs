"""
python program to get a string from a given string
where all occurrences if its first char have been changed ro $ ,
except the first char itself
"""
a=input('enter a string : ')
l=len(a)
for i in range(1,l):
    a.replace("b","$")
print(a)
        
