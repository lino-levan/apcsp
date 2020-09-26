import re
import functools

# Exercise 1
def both_positive(x, y):
    """
    Should return True if both x and y are positive. Correct the error.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x>0 and y>0

print("Both Positive")
print(both_positive(-1,1)) # false
print(both_positive(1,1)) # true
print("")

# Exercise 2
def check_condition(c1, c2, c3):
    """
    Takes in 3 boolean contexts (conditions) as input. Print
    'All true.' when all 3 are true. Print '2 true.' if only 2
    condtions are true. Print 'Only 1 true.' if 1 condition is true.

    Use boolean operators and if/elif/else conditions.

    >>> x = 3
    >>> y = 4
    >>> z = 5
    >>> check_condition(x == y, y > z, z == 4)
    None true.
    >>> check_condition(x > y, y < z, z == 5)
    Only 2 true.
    >>> check_condition(x < y, y < z, z == 5)
    All true.
    check_condition(x > y, y > z, z == 5)
    Only 1 true.
    """
    return "All true." if c1 and c2 and c3 else ("Only 2 true." if ((c1 and c2) or (c1 and c3) or (c2 and c3)) else ("Only 1 true." if c1 or c2 or c3 else "None true."))

x = 3
y = 4
z = 5
print("Check Condition")
print(check_condition(x == y, y > z, z == 4)) # None true.
print(check_condition(x > y, y < z, z == 5)) # Only 2 true.
print(check_condition(x < y, y < z, z == 5)) # All true.
print(check_condition(x > y, y > z, z == 5)) # Only 1 true.
print("")

# *** Write your own function for Exercise 3 here. ***
def any_number_seven(input_string):
    return "7" in input_string

print("Any Number 7")
print(any_number_seven("782132131")) # true
print(any_number_seven("214235434")) # false
print("")

# *** Write your own function for Exercise 4 here. ***
def jackpot(input_string):
    return "777" in input_string

print("Jackpot")
print(jackpot("1177177722")) # true
print(jackpot("1234")) # false
print(jackpot("1177177722")) # true
print("")

# *** Write your own function for Exercise 5 here. ***
def any_7x7(input_string):
    return False if re.search("7.7",input_string)==None else True

print("Any 7X7")
print(any_7x7("123707221")) # true
print(any_7x7("12370")) # false
print(any_7x7("abc787def")) # true
print("")

# Exercise 6
def repeated(f, n, x):
    """
    My previous terrible attempt:
    rc = x
    for i in range(0,n):
        rc = f(rc)
    """

    return functools.reduce(lambda x, y: f(x), [x]*(n+1))

def square(x):
    return x * x

def opposite(b):
    return not b

print("Repeated")
print(repeated(square, 2, 3)) # 81
print(repeated(square, 1, 4)) # 16
print(repeated(square, 6, 2)) # 18446744073709551616
print(repeated(opposite, 4, True)) # True
print(repeated(opposite, 5, True)) # False
print(repeated(opposite, 631, 1)) # False
print(repeated(opposite, 3, 0)) # True
print("")
