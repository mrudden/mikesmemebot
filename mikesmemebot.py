# lets test some scheduling

from datetime import *
import twitter
from secret import *

api = twitter.Api(consumer_key=key1,
                  consumer_secret=secret1,
                  access_token_key=key2,
                  access_token_secret=secret2)

test_mode = False

today = datetime.today()
day_of_the_week = today.weekday()
day_of_the_month = today.day
this_month = today.month
this_year = today.year

meme_path = "./memedb/"
meme_file = "nicememe.png"

#Test Zone
if test_mode:
    print("#testmodepleaseignore")
    print(day_of_the_week)
    print(day_of_the_month)
    print(this_month)
    print(this_year)

if day_of_the_week == 6:
    day_of_the_week = "Sunday"
elif day_of_the_week == 0:
    day_of_the_week = "Monday"
elif day_of_the_week == 1:
    day_of_the_week = "Tuesday"
elif day_of_the_week == 2:
    day_of_the_week = "Wednesday"
elif day_of_the_week == 3:
    day_of_the_week = "Thursday"
elif day_of_the_week == 4:
    day_of_the_week = "Friday"
elif day_of_the_week == 5:
    day_of_the_week = "Saturday"

if test_mode:
    print("Today is " + day_of_the_week)

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

if test_mode:
    print("This month is " + this_month)

daily_update = ""

print("\n------\n#dailyupdate\n------\n")
if day_of_the_week == 'Sunday':
    daily_update = "#SundayFunday"
if day_of_the_week == 'Monday':
    daily_update = "Only 7 more days until Monday!"
if day_of_the_week == 'Tuesday':
    daily_update = "Is it Wednesday yet?"
if day_of_the_week == 'Wednesday':
    daily_update = "It is Wednesday my dudes"
    meme_file = "wednesday.jpg"
if day_of_the_week == 'Thursday':
    daily_update = "Only 6 more days until Wednesday! #mydudes"
if day_of_the_week == 'Friday':
    daily_update = "#BurgersAndFryday"
if day_of_the_week == 'Saturday':
    daily_update = "ayy lmao"

print(daily_update)
try:
    status = api.PostUpdate(daily_update)
except:
    print("*~didn't work~*")

print("\n\n------\n#monthlyupdate\n------\n")
if (this_month == 'September') and (day_of_the_month == 1):
    print("Wake me up when September ends")
elif (this_month == 'September') and (day_of_the_month == 30):
    print("Okay Mr. Greenday you can wake up now!")

text_to_post = "test post please ignore #please"
meme_to_post = meme_path + meme_file
status = api.PostMedia(text_to_post, meme_to_post)
#status = api.PostUpdate("I am become twitter bot, destroyer of worlds")
