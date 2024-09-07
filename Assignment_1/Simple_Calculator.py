#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1: Simple Calculator

#Functions to perform basic Arithmetic operations
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Oops! You have entered the wrong number. Division by zero is not allowed."
    else:
        return a / b

def modulo(a,b):
    return a % b

#Function to check if user enters a valid number 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Function to get an operation from user
def get_operation():
    while True:
        operation = input("Enter the operation number between 1 to 5: ")
        if operation in ['1', '2', '3', '4','5']:
            return operation
        else:
            print("Invalid input. Please select a valid operation number between 1 to 5.")
            
#Main Function
def simple_calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        number1 = get_number("Enter the first number: ")
        number2 = get_number("Enter the second number: ")
        
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        
        operation = get_operation()
        
        if operation == '1':
            result = add(number1, number2)
            operator = '+'
        elif operation == '2':
            result = subtract(number1, number2)
            operator = '-'
        elif operation == '3':
            result = multiply(number1, number2)
            operator = '*'
        elif operation == '4':
            result = divide(number1, number2)
            operator = '/'
        elif operation == '5':
            result = modulo(number1, number2)
            operator = '%'
            
        print(f"Result: {number1} {operator} {number2} = {result}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation != 'yes':
            print("Goodbye!")
            break

# Run the calculator
simple_calculator()

