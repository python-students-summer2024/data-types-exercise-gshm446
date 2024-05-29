"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    total_sale=float(input("What is your estimated total sales？"))
    rate= 0.23
    profit=(total_sale * rate)
    answer=f'"Profit:{profit}" for sales of {total_sale}.'
    print(answer)


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    first_number=int(input("first number (please to put a integer)"))
    second_number=int(input("second number (please to put a integer)"))
    float= (first_number % second_number)
    times=int(first_number / second_number)
    answer=f"{second_number} goes into {first_number} a total of {times} times with a remainder of {float}."
    print(answer)


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles=float(input("Miles driven: "))
    gas=float(input("Gas used (gallons):"))
    mpg=(miles/gas)
    answer=f"Miles per gallon: {mpg}"
    print(answer)


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1= float(input("Enter the first price "))
    price2= float(input("Enter the second price "))
    price3= float(input("Enter the third price "))
    answer1= "{:.2f}".format(price1)
    answer2= "{:.2f}".format(price2)
    answer3= "{:.2f}".format(price3)
    message=f"Here are your prices!\n Price #1 :$ {answer1}\n Price #2:$ {answer2}\n Price #3:$ {answer3}"
    print(message)
