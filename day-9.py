#String Handling

# name = "hello world"

# print(name.upper())
# print(name.lower())
# print(name.title())
# # print(name.replace("W"," "))
# print(len(name))
# print(name.strip())
# print(len(name))
# print(name)


# text = "hello worl"

# print(text.upper())    # " HELLO WORLD"
# print(text.lower())    # " hello world"
# print(text.strip())    # "hello world"  (removes spaces)
# print(text.replace("world", "Python"))  # " hello Python "
# print(text.split())    # ['hello', 'world']
# print(text.find("w"))  # 7 (index of substring)
# print(text.startswith("h"))  # True
# print(text.endswith("d"))    # True



# print(name[::-1])


# a = "hello"
# b = " world"

# print(a+b)


# Palindrome Check

# text = "phone"

# if text == text[::-1] :
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")

# text= "python"

# print(len(text))

# Lambda

# s1 = 'GeeksforGeeks'
# s2 = lambda a: a.upper()
# print(s2(s1))


# def fun(a):
#     return a.upper()


#problem
a = 1
b=-1
flag = False

if (a >= 0 or b >= 0) and flag == False:
    print(True)
            
elif (a < 0 and b < 0 ) and flag == True:
    print(True)
else:
    print(False)