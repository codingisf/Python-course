# class Student:
#     def __init__(self, name, age):# constructor
#         self.__name = name
#         self.__age = age
        
        
        
# student1 = Student("Jeo", 20)


# print(student1.__name)  # Jeo
# print(student1.age)   # 20



# class Demo:
#     count = 0  # class variable

#     def __init__(self):
#         Demo.count += 1

#     @classmethod
#     def show_count(cls):
#         return cls.count

# d1 = Demo()
# d2 = Demo()
# print(Demo.show_count())



# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance  # private       --> 1000

#     def deposit(self, amount):
#         self._balance += amount                  #--> 1500

#     def get_balance(self):
#         return self._balance

# account = BankAccount(1000)

# account.deposit(500)

# print(account.get_balance())  # 1500
# # print(account.__balance)  # Error! Private attribute




# class Animal:                                           # parent class
#     def sound(self):
#         return "Some sound"

# class Dog(Animal):
#     def sound(self):
#         # parent_sound = super().sound()  # Calls Animal's sound()
#         # return parent_sound + "Bark"
        
#         return "Bark"

# dog = Dog()
# print(dog.sound()) 
#   # Bark
  
# a1 = Animal() 
# print(a1.sound())


# a1 = Animal
# print(a1.sound())
