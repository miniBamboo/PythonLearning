#if else三元表达式
score = float(input('score(0~100):'))
level  = '优秀' if score >= 90 else  '及格' if score >= 60 else '不及格'
print(score,level)
