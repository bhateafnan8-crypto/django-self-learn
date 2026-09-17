# """
# 🧪 Practice
# Create programs for:
# """

# #Question
# """
# 1. Calculate age
# """
# #solution
# print("--------------------------------------")

# birthyear = input("Enter your birth year: ").strip()
# age = 2026-int(birthyear)
# print(f"your age is : {age}")


# #Question
# """
# 2. Calculate salary after tax
# """
# #solution
# print("--------------------------------------")

# tax = 0.18
# sal = int(input("Enter your salary: ").strip())
# sal_aftertax = sal - tax
# print(f"your salary will be after tax : {sal_aftertax}")


# #Question
# """
# 3. Celsius → Fahrenheit
# """
# #solution
# print("--------------------------------------")

# celius = int(input("Enter temp in celcius : ").strip())

# Fahrenheit= (9/5 * celius) + 32.

# print(f"Fahrenheit temp : {Fahrenheit}")


# #Question
# """
# 4. Simple calculator
# """
# #solution
# print("--------------------------------------")

# choice = input("Enter your choice (+,-,*,/): ").strip()

# num1 = int(input("Enter num 1 : ").strip())
# num2 = int(input("Enter num 2 : ").strip())

# if choice == "+":
#     print(f"addition : {num1+num2}")
# elif choice == "-":
#     print(f"subtraction : {num1-num2}")
# elif choice == "*":
#     print(f"multiplication : {num1*num2}")
# elif choice == "/":
#     try:
#         print(f"division : {num1/num2}")
#     except ZeroDivisionError as e:
#         print(f"Error : {e}")
# else:
#     print("Invalid choice , try again!")


# #Question
# """
# 5. Check whether a number is positive/negative
# """
# #solution
# print("--------------------------------------")

# num = int(input("Enter num to check positivity: ").strip())

# if num % 2 == 0:
#     print(f"num is positive : {num}")
# else:
#     print(f"num is negative : {num}")


# #Question
# """
# 6. Calculate area of a rectangle
# """
# #solution
# print("--------------------------------------")

# height = int(input("Enter height of rectangle : ").strip())
# width = int(input("Enter width of rectangle : ").strip())

# area_of_rect = height * width

# print(f"area of rectangle is  : {area_of_rect}")


# """
# 🧪 Practice
# Build:
# """
# #Question
# """
# 1. Print 1–100
# """
# #solution
# print("--------------------------------------")

# for i in range(1,101):
#     print(i)



# #Question
# """
# 2. Even numbers
# """
# #solution
# print("--------------------------------------")

# for i in range(1,20):
#     if i % 2 == 0:
#         print(i)


# #Question
# """
# 3. Multiplication table
# """
# #solution
# print("--------------------------------------")

# for i in range(1,11):
#     print(i*2)


# #Question
# """
# 4. Sum of numbers
# """
# #solution
# print("--------------------------------------")

# num = 0
# for i in range(1,6):
#     num = num + i
# print(num)


# #Question
# """
# 5. Factorial
# """
# #solution
# print("--------------------------------------")

# # n = 5
# # r = 1
# # for i in range(1,n+1):
# #     r = r * i
    
# # print(r)

# n = 1

# for i in range(1,6):
#     n *= i
# print(n)


# #Question
# """
# 6. Prime-number checker
# """
# #solution
# print("--------------------------------------")

# user = int(input("Enter number to check prime or not : ").strip())

# # for i in range(1,10):
# #     if user % i == 0:
# #         print(f"Not prime : {user}")
# #     else:
# #         print(f"Prime : {user}")

# if user > 1:
#     for i in range(2,user):
#         if user % i == 0:
#             print(f"Not prime : {user}")
#             break
#     else:
#         print(f"Prime : {user}")
# else:
#     print(f"Not prime : {user}")


# #Question
# """
# 7. Number guessing game
# """
# #solution
# print("--------------------------------------")

# numbers = "0123456789"

# user_num = input("Guess the number : ").strip()

# if user_num in numbers:
#     print("Correct:",user_num)
# else:
#     print("Try again")


#Question
"""
1. Write a Python function
"""
#solution

print("--------------------------------------")

def greet():
    print("Hello")
greet()


#Question
"""
2. Use if/else
"""
#solution

print("--------------------------------------")

a = 10
if a > 10 :
    print("high")
else:
    print("perfect")


#Question
"""
3. Use a loop
"""
#solution

print("--------------------------------------")

for i in range(5):
    print(i)


#Question
"""
4. Manipulate a list
"""
#solution
print("--------------------------------------")

lst = []

print(lst)

user_inp = input("Enter number to insert : ")

lst.append(user_inp)

print(lst)


#Question
"""
5. Read/write dictionary data
"""
#solution
print("--------------------------------------")

dict1 = {"name":"adfar"}

print(f"name : {dict1['name']}")

dict1['age'] = 10

print(f"age : {dict1['name']}")


#Question
"""
6. Build a small calculator
"""
#solution
print("--------------------------------------")

op = input("Enter your operator (+,-,*,/) : ")
n1 = int(input("Enter num 1 : "))
n2 = int(input("Enter num 2 : "))

if op == "+":
    print(f"add : {n1+n2}")
elif op == "-":
    print(f"sub : {n1-n2}")
elif op == "*":
    print(f"mul : {n1*n2}")
elif op == "/":
    try: 
        print(f"div : {n1/n2}")
    except ZeroDivisionError as e:
        print(f"Error : {e}")
else:
    print("invalid operator , try again")


