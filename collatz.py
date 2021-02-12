#User Inputs a number abs convert the number to a positive number in case user enters a negative number
num = abs(int(input ("Please enter a positive integer: ")))
#Initialize a list of the numbers to print at the end
lst = [num]
#while num is greater than 1 keep running
while int(num) > 1:
    #Create logic requested (If mod equals 0 we divide the number by 2 and add to the list as a integer)
    if((num%2) == 0):
        num = (num/2)
        lst += [int(num)]
    else:
    #If the number is odd (mod != 0) we multiply by 3 and add 1, then we add the number to the list
        num = ((num*3)+1)
        lst += [int(num)]
    #output a list of the numbers calculated
print(str(lst))
