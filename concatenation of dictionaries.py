#d1={"a":1,"b":2}
#d2={"c":3,"d":4}

d1={}
x=int(input("enter number of records: "))
for i in range(x):
    key=input("enter key: ")
    value = input("enter value: ")
    d1[key] = value
print(d1)

d2={}
y=int(input("enter number of records: "))
for i in range(y):
    key=input("enter key: ")
    value = input("enter value: ")
    d2[key] = value
print(d2)
# d={}
# for i in d1:
#    d[i]=d1.values()
# for j in d2:
#     d[j]=d2.values()
# print(d)
# ******************************** alternate way************************
# d={**d1,**d2}
# print(d)
d={}
for i in d1.items():
    d[i[0]] = i[1]
for j in d2.items():
    d[j[0]] = j[1]

print(d)