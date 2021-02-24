# This function calculates a Square root based on Newton estimate formula

import math

def sqrt(n):
    tolerance = 0.00001 # This is the precision Variable
    estimate = 1.0 # initialize the estimate variable

    while True:
        estimate = (estimate + n / estimate) / 2 #This is actually the newton formula to calculate a sqrt
        diference = abs (n - estimate ** 2) #Get the absolut number from the subtraction
        if diference <= tolerance: # Compare the results with the precision
            break
    return estimate #Return the estimation

#The main Function is called for the user to enter the inputs and print out the outputs
#Just to compare the program outputs the math.sqrt funcition

def main():
    while True:
        n = input('Enter a Number (q to quit): ')
        if (n.lower()) == "q":
            break
        n = float(n)
        print(f"The Newton Estimate is: {sqrt(n)}")
        print(f"The Math function in Python Estimate is: {math.sqrt(n)}")

#Calling the main funcition    
main()
    

    
    
    
