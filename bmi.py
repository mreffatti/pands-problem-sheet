#BMI Calculator
#Marcelo Reffatti
#Version 0.1
#Validating if the imput is an integer
while True:
    try:
        height = int(input ("Enter your height in Centimeters "))
        weight = float(input ("Enter your weight in kg "))
    except ValueError:
        #If not an interger entering contimue looping
        print("That's not a number!")
    else:
        #Validation sucessfull exiting the loop
        break
#Calculating BMI formula
bmi = "{:.2f}".format(weight/((height/100)**2))

#Print Output
print(f"The Body Mass Index for a person of {(height/100)}m height and weighting {weight}kg  is {bmi}")