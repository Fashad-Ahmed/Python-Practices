def gen(n):
    for i in range(n):
        yield i

for i in gen(100000):
    print(i)

def gen(n):
    for i in range(n):
        yield i

ob1 = gen(4)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))

num = "abcd"
iter1 = iter(num)
print(next(iter1))
print(next(iter1))