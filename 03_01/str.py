# str_hello = "Hello"
# test_mess = "hello, Name!\nNice to meet you!\n"
test_mess = input()
dig_mess = "ra1234aa"

# print(test_mess.count("\n"))
# str_hello = str_hello.join("!")
print()
split_mess = test_mess.split("Name")
print(split_mess[0], "Nike", split_mess[1])
str_hello = "Tod".join(split_mess)

print(str_hello)
print("[5:]", str_hello[5:])
print("[:5]",str_hello[:5])
print("[-5:]",str_hello[-5:])
print("[:-5]",str_hello[:-5])
# print(str_hello[])
