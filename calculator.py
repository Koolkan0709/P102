x = float(input("enter a number: "))
y = float(input("enter another number: "))
z = input("enter operation: ")
w = 0
if z == "+" :
    w = x + y
    print(w)
elif z == "-" :
    w = x - y
    print(w)
elif z == "*" :
    w = x * y
    print(w)
elif z == "/" :
    w = x / y
    print(w)

else :
    print("That's Nonsense man!!")

