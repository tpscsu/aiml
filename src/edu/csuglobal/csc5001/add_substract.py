# The below program accepts two numbers from terminal num1 and num2
# Adds the two numbers and output the result on the terminal
# Subtract the numbers in both ways and output the results on the terminal
# The program will terminate with an error message if a non-numeric input is provided


try:
    num1 = int(input('Enter the first number : '))
    num2 = int(input('Enter the second number : '))
    total = num1 + num2
    difference = num1 - num2
    print(num1, '+', num2, '=', total)
    print(num1, '-', num2, '=', difference)
except ValueError:
    print('Invalid Inputs - Expected a number')
    exit()
