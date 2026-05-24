data = [1,2,3,4]
A = [items*2 if 
    items % 2 == 0 else 
    items for items in data]
B = [items*2 
    for items in data 
    if items % 2 == 0]

print(A)
print(B)