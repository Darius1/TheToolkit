## A simple calculator that can perform basic math functions
## These functions are addition, subtraction, multiplication, and division
import msvcrt

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number


print "Welcome to the Calculator!"
print "You can add, subtract, multiply, and divide. Just type the number of the option that you want to perform!"


while True :

    print "\n"
    print "1. Add"
    print "2. Subtract"
    print "3. Multiply"
    print "4. Divide"

    print "\n"
    choice = int(raw_input("What option? "))

    print "\n"

    num1 = int(raw_input("First Number: "))
    num2 = int(raw_input("Second Number: "))

    if choice == 1:
        print "%d + %d = %d" % (num1, num2, add(num1, num2))
    elif choice == 2:
        print "%d - %d = %d" % (num1, num2, subtract(num1, num2))
    elif choice == 3:
        print "%d * %d = %d" % (num1, num2, multiply(num1, num2))
    elif choice == 4:
        print "%d / %d = %d" % (num1, num2, divide(num1, num2))
    else:
        print "Please enter a valid number choice"

    input = raw_input("\nPress any key to continue, 0 to quit: ")

    if input == '0':
        break
