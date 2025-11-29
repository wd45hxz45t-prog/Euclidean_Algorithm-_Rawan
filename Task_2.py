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
print("The Greatest Common Denominator is", gcd(48, 18))