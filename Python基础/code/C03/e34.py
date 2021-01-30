# 1. 输入苹果单价
price_str = input("请输入苹果价格：")
# 2. 要求苹果重量
weight_str = input("请输入苹果重量：")
# 3. 计算金额
# 1> 将苹果单价转换成小数
price = float(price_str)
# 2> 将苹果重量转换成小数
weight = float(weight_str)
# 3> 计算付款金额
money = price * weight
print(money)
