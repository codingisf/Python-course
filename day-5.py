# Looping practice


# No of rows = No of columns

# for i in range(1,6):     #Rows          
    
#     for j in range(0,i):    #column     
#         print(i , end = " ")
        
#     print()
        
# print("Hello" , end = " to ")
# print("world")
        
# loop - 1

# i = 1
# range(1,1)  -> j = 1

#  loop - 2

# i = 2
# range (1,2)  -> j = 1 , j = 2

#  loop - 3

# i = 3
# range (1,3)  -> j = 1 , j = 2 , j = 3

#  loop - 4

# i = 4
# range (1,3)  -> j = 1 , j = 2 , j = 3 , j = 4

#  loop - 5

# i = 5
# range (1,3)  -> j = 1 , j = 2 , j = 3 , j = 4 , j = 5




# Prime number

# num = 6

# for i in range(2,num):
#     if num % i == 0 :
#         print("Its not a prime number")
#         break
        
# else:
#     print("Its a prime number")



# num = 9 
# if num % 3 == 0:
#     print("its not a prime number")
    
# else:
#     print("its a prime number")
    
    
# num = 23

# for i in range(2,num):
#     if num % i == 0:
#         print("its not a prime number")
#         break
        
# else:
#     print("Its a prime number")

n = 4

if n > 0:
        for i in range(n-1,-1,-1):
            print(i , end = " ")
else:
    print ("already Zero")