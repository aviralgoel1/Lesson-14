import datetime
import calendar

x=1
for x in range (1,13):
    m=datetime.date(2025,x,1).strftime("%B")
    print(m)
