
x=int(input("enter character:  "))
list1=[]
for i in range(x):
    a=int(input("ennter number:  "))
    if type(a) == int:
        list1.append(a)
    else:
        continue

final=[]
for i in list1:
    if i not in final:
        final.append(i)

print(final)