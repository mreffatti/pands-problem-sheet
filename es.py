#Module has a method to get the paramenter from a command line
import sys

#Fuction to count the number of e's - Passing the name of the file
def countes(arq):
    with  open(arq, 'r') as f:  #Open the file as readonly
        text = f.read() #Set a variable to the file text
        count = 0 #initialize counter variable
        totalcount = 0 #initialize totalcounter variable
    #loop for looking for e's
        for char in text:
            totalcount += 1
            if char.lower() == 'e': #If e is found increment the counter
                count += 1
        print(f"There are a total of {totalcount} characters which of {count} are e's in {arg}") #Output the total number of characters, number of e's and the file name

#Set a variable with the second element of the array which is the text file. The first element of the array is the name of the program
arg = sys.argv[1]
#Call a function to count e's passing the name of the text file
countes(arg)