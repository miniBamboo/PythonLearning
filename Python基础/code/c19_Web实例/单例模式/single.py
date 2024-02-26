Testing = True
class First(object):
    def test(self):
        print("First self id",id(self))
class Second(object):
    def test(self):
        print("Second self id",id(self))
t= None
if Testing:
    t = First()
else:
    t = Second()
#print(id(t))

