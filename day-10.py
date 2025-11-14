# File Handling

# file = open("./folder/text.txt",'a')

# file.write("\nthis is day 12 of python class !")

# # print(content)

# file.close()


# with open("text.txt",'w') as file :
#     # content = file.read()
#     # print(content)
#     file.write("\nthis is day 12 of python class !")

# print("the File handling is ended")


# -----------------------------------------------------------------

# Modules

# import math

# print(math.log(10))

# Number guessing game

# import random

# number = random.randint(1,100)


# guess = 5

# while guess != 0: 
    
#     choice = int(input("enter your choice (1 - 100) :"))
    
#     if choice == number:
#         print(f"The number is {number} You win !")
#         break
#     else:
#         print("Worng choice try again")
        
#         if number > choice:
#             print("Your guess is low")
            
#         else:
#             print("Your guess is high")
    
#     guess -= 1
    
# else:
#     print(f"The number is {number}")

# -------------------------

# import random 

# choices = ["apple" , "orange" , "banana"]

# print(random.choices(choices))


# -----------------------------------------------------------------

# Error handling

# a = 10
# b = 10



# try :
#     c = a/b
#     print(c)

# except:
#     print("any number can't be divided by zero")
    
# finally:
#     print("the error handling is finished")

# ----------------------------------------------------------
# costum error


# class AgeError(Exception):
#     pass


# age = int(input("Enter age: "))

# if age <= 18:
#     raise AgeError("Age must be 18 or above!")

# else:
#     print("Valid age")

# x = 10
  
# i = 2
# while(i < x):
#         #code here
#     print (i)
    
    
        
        