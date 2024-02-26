#输出字符串型的date和时间型的date
from datetime import datetime
datesource = "2019年4月26日 16:47"
dt=datetime.strptime(datesource,'%Y年%m月%d日 %H:%M')
print(dt)
print(type(dt))
