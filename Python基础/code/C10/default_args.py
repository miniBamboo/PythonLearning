#默认值参数---参数默认值
'''
def line(char='*',n=80):
    print(char*n)
line()
line('-')
line('#')
line('>',66)
line('<',71)
line('=',62) #关键字参数
'''
#必须参数a
def sum4data(a, b=4, c=5,d=6):
    #必须参数,即没有默认值的参数在参数列表中尽量靠左
    #有默认值的参数在参数列表中尽量靠右
    #即有默认值的参数的右侧不能有必须参数，必须参数左侧不能有有默认值的参数 
    s = a + b + c + d
    print(s)
#sum4data() #少必须参数
sum4data(3)
#3+4+5+9
sum4data(3,d=9) #d=9关键字参数
#1+2+5+6
sum4data(3,b=2) #b=2关键字参数
