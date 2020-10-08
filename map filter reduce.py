from functools import reduce

# map ( func. to apply, no. of inputs)
def cube(x):
    return x**3

l1 = [1,2,3,4,5,6]
l2 = list(map(cube,l1))
# TYPE-CASTED IN LIST
print(l2)

def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

h1 = [1,2,3,4,5,6,7,-2,-5]
greater_th_2 = list(filter(greater_than_2, h1))
print(greater_th_2)


def string_sum(a, b):
    return a+b

newstring = reduce(string_sum, ["You", " are", " human"])
print(newstring)
sum_x = reduce(string_sum,h1)
print(sum_x)