import random
import time 

def randomdate(startdate,enddate):
    print("printing random date between ",startdate, " and ",enddate )
    randomgen=random.random()
    dateFormat= '%m/%d/%Y'

    starttime=time.mktime(time.strptime(startdate, dateFormat))
    endtime=time.mktime(time.strptime(enddate, dateFormat))

    randomtime=starttime+randomgen*(endtime-starttime)
    randomdate=time.strftime(dateFormat,time.localtime(randomtime))
    return randomdate

print ("random date = ", randomdate("1/1/2016","12/12/2025"))