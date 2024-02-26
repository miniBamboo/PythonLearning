class Site: 
    def __init__(self, name, url):
         self.name = name # public
         self.__url = url # private 
    def who(self):
         print('name : ', self.name)
         print('url : ', self.__url) 
    def __foo(self): # 私有方法
        print('这是私有方法') 
    def foo(self): # 公共方法
        print('这是公共方法') 
        self.__foo() 
x = Site('Python学习网', 'www.pythonlearning.com') 
x.who() # 正常输出 
x.foo() # 正常输出 
x.__foo() # 报错

