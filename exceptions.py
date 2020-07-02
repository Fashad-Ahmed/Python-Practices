try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
except Exception as e:
    print("sahi number daluu bhai!")
except ZeroDivisionError:
    print("sahi num daluu na yr")
except ValueError:
    print("same data type dalu")
else:
    print("contact ur boss")
finally:
    print("thank you")


