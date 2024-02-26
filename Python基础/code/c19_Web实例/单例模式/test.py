from single import t as t1
print(t1,id(t1))

from single import t as t2
print(t2,id(t2))

t1.test()
t2.test()
