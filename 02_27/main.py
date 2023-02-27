print("Input A + B")

a = int(input("A: "))
b = int(input("B: "))
ch = input("Operator :")

if ch == "+" :
    res = a + b
elif ch == "//" :
    res = a // b
elif ch == "/" :
    res = a / b
elif ch == "%" :
    res = a % b


if a > 0 :
    print("a > 0")
elif a == 0 :
    print("a == 0")
else :
    print("a < 0")

print("Hello world", res , "!")
