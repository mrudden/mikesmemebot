# lets test some scheduling

from datetime import *

test_mode = False

today = datetime.today()
day_of_the_week = today.weekday()
day_of_the_month = today.day
this_month = today.month
this_year = today.year


#Test Zone
if test_mode:
    this_month = 9
    day_of_the_month = 1

if day_of_the_week == 0:
    day_of_the_week = "Sunday"
elif day_of_the_week == 1:
    day_of_the_week = "Monday"
elif day_of_the_week == 2:
    day_of_the_week = "Tuesday"
elif day_of_the_week == 3:
    day_of_the_week = "Wednesday"
elif day_of_the_week == 4:
    day_of_the_week = "Thursday"
elif day_of_the_week == 5:
    day_of_the_week = "Friday"
elif day_of_the_week == 6:
    day_of_the_week = "Saturday"

if this_month == 1:
    this_month = "January"
elif this_month == 2:
    this_month = "February"
elif this_month == 3:
    this_month = "March"
elif this_month == 4:
    this_month = "April"
elif this_month == 5:
    this_month = "May"
elif this_month == 6:
    this_month = "June"
elif this_month == 7:
    this_month = "July"
elif this_month == 8:
    this_month = "August"
elif this_month == 9:
    this_month = "September"
elif this_month == 10:
    this_month = "October"
elif this_month == 11:
    this_month = "November"
elif this_month == 12:
    this_month = "December"

print("------\n#dailyupdate\n------")
if day_of_the_week == 'Wednesday':
    print("It is Wednesday my dudes")

print("------\n#monthlyupdate\n------")
if (this_month == 'September') and (day_of_the_month == 1):
    print("Wake me up when September ends")
elif (this_month == 'September') and (day_of_the_month == 30):
    print("Okay Mr. Greenday you can wake up now!")
