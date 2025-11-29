
#task_2:


# defines a function called gcd that takes inputs a and b
def gcd(a, b):
    # loops till or as long as b is not 0
    while b != 0:
        #calculates the remainder of a divided by b
        remainder= a % b
        # a becomes b so the numbers are shifted down one step
        a = b
        # b becomes remainder
        b = remainder
        """loop ends when b is 0 and the function returns returns
        a which is the GCD"""
    return a

# the gcd function above is called and it prints the result which is a
print("The Greatest Common Divisor is", gcd(48, 18))





#task_4:


# defines a function called gcd that takes inputs a and b
def gcd(a, b):
    # loops till or as long as b is not 0
    while b != 0:
        #calculates the remainder of a divided by b
        remainder= a % b
        # a becomes b so the numbers are shifted down one step
        a = b
        # b becomes remainder
        b = remainder
        """loop ends when b is 0 and the function returns returns
        a which is the GCD"""
    return a


# a loop that will continue until the user enters a valid data type and number
while True:
    #asks the user to enter the first number as a string
    a = input("Enter the first number: ")
    # asks the user to enter the second number as a string
    b = input("Enter the second number: ")

 #checks if a or b have a decimal point
    if "." in a or "." in b:
        #dispalys error message since  GCD cannot be a decimal point
        print("Integer cannot be decimals, Please, try again.")
        # the loop continues and allows the user to input a different number
        continue
#a statement that allows the program to run a code that may cause an error and instead
     #of crashing it informs the user of the error and the program continues
    try:
        #attemps to convert a input to an integer
        a = int(a)
        #attemps to convert b input to an integer
        b = int(b)
        #if converting fails because the user used the wrong data type, it runs this block of code
    except ValueError:
        #displays an error message to the user, telling them it must be an integer only"
        print("You must enter integers only. Try again.")
        # loop is returned and continues to ask the user for inputs
        continue

     # if statement that checks if either inputs are negative
    if a < 0 or b < 0:
        # if either inputs are negative, it prints an error message telling the user to try again"
        print("Integer cannot be negative, Please try again.")
        # loop is returned and the user is asked for input again
        continue

  # if the input the user has entered is valid and passes the checks, it leaves the while loop
    break



# the gcd function above is called and it prints the result which is a
print("The Greatest Common Divisor is", gcd(a, b))