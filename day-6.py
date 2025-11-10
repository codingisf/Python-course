# name = "Jeo"    #global scope


# def fun(a,b):           #parameters
#     return a + b
    
# result =  fun(10,5)     #arguments

# print(result)

def getting_age():
    
    age = int(input("enter your age : "))
    return age



def checking_age(age = 18):             # Default agrv
    
    if age >=18:
        print("Your eligable")
    else:
        print("Your not eligable")
        
        

age1 = getting_age()            #  the functions returning something

checking_age(age1)

# def greets(Fname , Lname):
#     print("hello" , Fname,Lname)
    
# greets(Lname="smith",Fname="jhon")


# calculator 
# using functions
# choice is users wish (+,-,*,/)
# you need to create a four funtions add() , sub() , ......


# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# choice = input("Enter your choice (+,-,*,/) : ")

# if choice == '+':
#     print(a+b)
# elif choice == '-':
#     print(a-b)
# elif choice == '*':
#     print(a*b)
# elif choice == '/':
#     print(a/b)
    
# else:
#     print("worng Choice : " , choice)


