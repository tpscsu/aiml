# The below program accepts two numbers from terminal num1 and num2
# Multiplies the two numbers and output the result on the terminal
# Divides num1 by num2 and output the result on the terminal
# The program will terminate with an error message if a non-numeric input is provided


try:
    num1 = int(input('Enter the first number : '))
    num2 = int(input('Enter the second number : '))
    product = num1 * num2
    quotient = num1 / num2
    print(num1, '*', num2, '=', product)
    print(num1, '/', num2, '=', quotient)
except ValueError:
    print('Invalid Inputs - Expected a number')
    exit()