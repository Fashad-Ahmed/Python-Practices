import bisect

lis = [1,2,5,10,15,17,28,35,59,61]
print(bisect.bisect(lis, 55))
bisect.insort(lis, 55)
print(lis)


lis1 = ["a","e", "h", "m", "o", "s"]
print(bisect.bisect(lis1, "k"))
bisect.insort(lis1, "k")
print(lis1)

