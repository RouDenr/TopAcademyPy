while True :
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
    else :
        break

    print("Hello world", res , "!")
