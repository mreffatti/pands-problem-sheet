# import module for dateand time
from datetime import datetime
from datetime import timedelta # You can play around by adding or substract dates

# Create a dictionary to mapp function datatime to days of the week
weekdays = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Sartuday", 6:"Sunday"}

#Get today's date
date = (datetime.now()) #+ timedelta(days=5)  
#Extract today's day (could be done in the same line above also)
day = date.weekday()

#test to see if today is weekday day <5 of weekend day == 6 or day == 7
if day < 5:
    print(f'unfortunately today is {weekdays[day]}, a weekday.')
else:
    print(f'Whohoo!!! Today is {weekdays[day]}, the weekend.')

print(f'This could also be done without dictionary using metod strftime from Datetime: {date.strftime("%A")}')
