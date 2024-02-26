import time
print (time.time()) #获取当前时间的浮点值，单位为秒
print ( time.ctime() )
print (time.localtime (time.time() ) )

gmt = time.gmtime()      #UTC格式的时间(时间元组)
print (gmt)
ftime1=time.mktime(gmt)
print (ftime1)            #将UTC格式的时间(时间元组)转化为时间戳
lt = time.localtime()      #所在时区当前时间(时间元组)
print (gmt)
ftime2=time.mktime(lt)
print (ftime2)            #将所在时区当前时间(时间元组)转化为时间戳

t = time.time()           #时间戳
print (time.gmtime(t))     #将时间戳转化为UTC格式的时间
print (time.localtime(t))    #将时间戳转化为当前时区时间

lt = time.gmtime()                         #UTC格式当前时区时间
st = time.strftime("%b %d %Y %H:%M:%S", lt)
print(st)
