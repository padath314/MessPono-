import json
from datetime import datetime

dt = datetime.now()
hour = dt.hour
minute = dt.minute
time = hour*60+minute

f= open('menu.json')

data = json.load(f)
 
meal = "mess closed"
if(time < 570):
    meal = "Breakfast"
elif(time < 840):
    meal = "Lunch"
elif(time < 1080):
    meal = "Snacks"
elif(time < 1260):
    meal = "Dinner"

day = dt.weekday()

if( day == 0):
    Day = "MON"
elif( day == 1):
    Day = "TUE"
elif( day == 1):
    Day = "WED"
elif( day == 1):
    Day = "THU"
elif( day == 1):
    Day = "FRI"
elif( day == 1):
    Day = "SAT"
else:
    Day = "SUN"


if(meal == "mess closed"):
    print("mess closed")
else:
    print(data[Day][meal]+data["DAILY"][meal])

f.close()