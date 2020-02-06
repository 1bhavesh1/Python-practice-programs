# program to swap keys and values of dictionary in python

Dict = {'A':12, 'B':13, 'C':14, 'D':15}

newDict = dict([(value,key) for key,value in Dict.items()])

print('\nOriginal dictionary is : \n')
print(Dict)

print('\nDictionary after swapping is : \n')
print("keys : values ")
for i in newDict:
    print(i," : ",newDict[i])
    
