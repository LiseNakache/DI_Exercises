from random import randint


def get_num(): 
    """
    returns a random integer between 1 and 10
    """
    number = randint(1, 10)
    return number


def pwr(func):
    """
    calculates the power of 2 a number returned by a function and print the original number as well as its power(2).
    #args: takes the argument func for function.
    """
    number = func()
    print(number, number*number)

# calling power function with get_num function as argument. Output: Random number to the power of 2
pwr(get_num)

