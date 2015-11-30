#coding: UTF-8
import datetime

myBirthday = datetime.date(1995, 12, 21)
toDay = datetime.date.today()

myLife = toDay - myBirthday

print myLife
print myLife.days
print myLife.days / 365
