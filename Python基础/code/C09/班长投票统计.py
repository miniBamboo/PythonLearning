votes_str="韩梅梅,李雷,张三,Jhon,李雷,韩梅梅,Jhon,李雷"
votes=votes_str.split(',')
print(votes)
result={}
for v in votes:
    result[v] = result.get(v,0)+1
print(result)
