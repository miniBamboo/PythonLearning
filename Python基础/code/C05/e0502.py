#if elif 的使用
holiday_name = input("今天是什么日子:") # "平安夜" #
if holiday_name == "情人节":
    print("买玫瑰，看电影")
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日!!")
