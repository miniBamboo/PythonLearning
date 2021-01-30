#字典遍历
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}
#for k in xiaoming:
#    print("{}:{}".format(k,xiaoming[k]))
    
for k,v in xiaoming.items():
    print("{}:{}".format(k,v))
