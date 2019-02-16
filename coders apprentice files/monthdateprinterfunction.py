#
#


import datetime

def addDays(year, month, day, dayincrement):
    startdate = datetime.datetime(year, month, day)
    enddate = startdate + datetime.timedelta( days = dayincrement)
    return enddate.year, enddate.month, enddate.day


y, m, d = addDays(2019, 9, 12,55)
print("{}/{}/{}".format(y, m, d))
