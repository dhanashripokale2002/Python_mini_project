#WAP using python to build a simple calculator
# Three step to build calculator
# 1.functions for operations 
# 2.user input
# 3.print result

#step 1 -create function
# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def sub(num1, num2):
    return num1 - num2

# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# function to mean two numbers
def avg(num1, num2):
    return (num1 + num2)/2

#step - 2: user input
print("Please select a operation: \n" \
      "1. Addition\n"  \
      "2.Substraction\n" \
      "3.Multiplication\n" \
      "4.Division\n" \
      "5.Average\n" ) 

select = int(input("Select a operation you want to perform from 1 to 5:"))
number1 = int(input("enter value num1:"))
number2 = int(input("enter value num2:"))

#step 3 : print the result

if select == 1:
    print("Sum of ",number1,"+",number2 ," is :", \
          add(number1,number2))
elif select == 2:
    print("Subtraction of ",number1,"-",number2 ," is :", \
          sub(number1,number2))
elif select == 3:
    print("mutiplication of ",number1,"*",number2 ," is :", \
          multiply(number1,number2))
elif select == 4:
    print("division of ",number1,"/",number2 ," is :", \
          divide(number1,number2))
elif select == 5:
    print("mean of (",number1,"+",number2 ,")/2 is :" , \
          avg(number1,number2))
else:
    print("Invalid operation!! plz try again")
