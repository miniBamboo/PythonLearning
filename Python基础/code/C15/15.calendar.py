import calendar
#打印每月日期
c = calendar.calendar(2021)
#print(c)
cm=calendar.month(2021,9)
#print(cm)
#import calendar

cw=calendar.weekday(2021,9,27)
#print(cw)
#import calendar
tps = (2021,9,10,11,35,0,0,0)
stamp = calendar.timegm(tps)
#print(stamp)

