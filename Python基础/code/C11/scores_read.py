f = open("scores.txt","rt")   #t表示文本文件方式
scores_str=f.read()
f.close()

print(scores_str)
print(type(scores_str))
scores=eval(scores_str)
'''#split+map+list:
score_str_ls = scores_str.split(',')
print(score_str_ls)
scores = list(map(float,score_str_ls))
'''
print(scores)
print(sum(scores)/len(scores))
