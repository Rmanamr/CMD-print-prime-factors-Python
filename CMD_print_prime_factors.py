"""Python CMD program for printing prime factors of a number.
using Python version 3.12.0
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
    """
    main function for interacting with the user
    """
    while(True):
    # while loop to keep the program running

        print("Please enter a number to calculate its prime divisors:")
        input_Number = int(input())
        # casting the input string into integer

        divisors = calculate_Divisors(input_Number)
        # passing the input_Number to the calculate_Divisors function and storing the result in divisors variable

        prime_Divisors = []
        for divisor in divisors:
            if(is_Prime_Number(divisor)):
                prime_Divisors.append(divisor)


        print("Prime factors of ", input_Number, " are:")
        array_Printer(prime_Divisors)
        # passing the result to the array_Printer to print each array element in a line

        print("***********************************************************")


def calculate_Divisors(number):
    """
    function for calculating divisors of the entered number.
    @param number: the number to calculate its divisors.
    @type number: integer
    @examples: 
     >>> calculate_Divisors(25)
         [1, 5, 25]
     >>> calculate_Divisors(7)
         [1, 7]
    """
    divisors = []

    if(number != 1):
        divisors.append(1)
        # number 1 is a divisor for all numbers

    divisor = 2
    while (divisor <= number / 2):
        if(number % divisor == 0):
            divisors.append(divisor)
        divisor += 1

    divisors.append(number)
    # any number can be divided by itself.
    
    return divisors


def is_Prime_Number(number):
    """
    function for checking whether a number is prime or not.
    @param number: the number to check.
    @type number: integer
    @examples: 
     >>> is_Prime_Number(7)
         True
     >>> is_Prime_Number(8)
         False
    """
    divisors = []
    divisor = 2
    while (divisor <= number / 2):
        if(number % divisor == 0):
            divisors.append(divisor)
        divisor += 1
        
    if(len(divisors) == 0):
        return True
    else:
        return False
    # a prime number has only 2 divisors, number 1 and the number itself, we start divisin by 2 and end by (number/2)
    # so if the divisors list is empty, it's a prime number.


def array_Printer(array):
    """
    function for printing each array element in a line.
    @param array: an array of elements.
    @type array: anything like integer, double and string.
    @examples: 
         array_1 = []
         array_2 = [1, 2, 3]
     >>> array_Printer(array_1)
          
     >>> array_Printer(array_2)
         1
         2
         3
    """
    for element in array:
        print(element)


if __name__ == '__main__':
    main()
    # run the main function after executing this file