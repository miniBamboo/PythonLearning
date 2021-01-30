scores_str="62 31 47 78 99 82"
#scores=[62,31,47,78,99,82]
scoress = scores_str.split()
scores = map(int,scoress)
result={}
for v in scores:
    #v=int(v)
    if v>=60:
        result['及格'] = result.get('及格',0)+1
    elif v<60:
        result['不及格'] = result.get('不及格',0)+1
    else:
        print('Error scores')
print(result)
