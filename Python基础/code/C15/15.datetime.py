import datetime
# 打印当前，年，月，日
print(datetime.date.today() )
#打印当前时间，精确到微秒
current_time = datetime.datetime.now() 
print(current_time)

#加十天
print (datetime.datetime.now() +datetime.timedelta (days=10) )
#减十天
print(datetime.datetime.now() +datetime.timedelta (days=-10))
#减十个小时
print(datetime.datetime.now() +datetime.timedelta (hours=-10))
#加120s
print(datetime.datetime.now() +datetime.timedelta (seconds=120))

