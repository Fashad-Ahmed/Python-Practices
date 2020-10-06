def fun(*args):
    print("Hello ",args[0],",",args[1],"and",args[2])
    print(type(args))

fun("jane","jake","john")

list_1 = ["sam","alex","cody"]
fun(*list_1)


def showMarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

list_2 = {"adlas":20 , "adler":36 , "lolla":41 , "ellenberg":46}
showMarks(**list_2)

print("\t ****************************************")

def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

master(5,*list_1,**list_2)