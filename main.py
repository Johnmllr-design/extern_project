user = "John"           # declaring the user to be John
age = 21                # declaring the age to be 21
height = "6.1"          # 

print("hello! I'm " + user + " and I am " + str(age) + " years old and " + height + " feet tall")   # pring with a kind message

num1 = 100              # declaring num1 to be 100
num2 = -12              # declaring num2 to be -11

print("the sum of num1 and num2 is", num1 + num2)   # summing num1 and num2 with a kind message
print("\n")                                         # print out a newline to give space for prompt

number = input("give me a number, and i'll describe it to you")     # call for user input
number = int(number)                                                # convert input to integer

if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")