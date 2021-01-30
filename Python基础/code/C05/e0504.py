#if的嵌套
has_ticket = False
if has_ticket:
    knife_length = int(input('刀子长度:'))
    if knife_length > 20:
        print("安检不通过")
    else:
        print("安检通过")
else:
    print('没票,不能进站')
