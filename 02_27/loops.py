import random

def print_arr(arr) :
    for i in arr :
        print(i, end="\t")
    print()


def main() :
    arr = []
    size = int(input("size : "))

    for i in range(0, size) :
        arr.append(random.randint(-100, 100))

    print_arr(arr)

    # while_else()
    # while_else(15)
    # print_all_negativ(n, 15)



# find all negativ
def print_all_negativ(n, size) :
    for i in range(n, size) :
        if i < 0 :
            print(i)

# while n != 0 :
#     print(n)
    # n -= 1

def while_else(n=100) :
    while n > 0:
        print(n)
        n -= 1
        t = input()
        if t == "e" :
            break
    else :
        print ("Else")

# for i in range(0, 11, 2) :
#     print(i)

# n = int(input())

# if n < 0 or n >= 100 :
#     print("Hell")


# if n > 0 and n % 2 == 0 :
#     print("lol")

# for i in range(10, 0, -1) :
#     print(i)

n = -10
main()
