from peewee import *
from sanic.log  import logger
import logging
 
import os,sys
import json
import sqlite3
 
import config as const
from config import db_setting
from datetime import datetime

logger.setLevel(logging.DEBUG)

db = None #单例模式
if const.TESTING:
    flag=os.path.exists(const.SQLITE_FILE_DIR)
    if flag==False:
        os.makedirs(const.SQLITE_FILE_DIR)    
    path= os.path.join(const.SQLITE_FILE_DIR , const.SQLITE_FILE)  # constants.DATA_FILE_DIR + os.path.sep +cfg["dbUrl_sqlite"]
    print(path)
    db = SqliteDatabase(path)
else: 
    db = MySQLDatabase(const.MYSQL_DB_NAME, **db_setting)


class BaseModel(Model):
    class Meta:
        database = db #  这个模型使用 "dbUrl_sqlite"数据库---------------------
class Init(BaseModel):#数据库初始化标志
    init = IntegerField(verbose_name='初始化标志', default=0)
 
class AdminUser(BaseModel):    
    #user_id = AutoField(primary_key=True, verbose_name='编号')# 定义自增
    phone = CharField(verbose_name='电话号码', max_length=64, null=False, index=True, primary_key = True)
    password = CharField(verbose_name='密码', max_length=256, null=True) #password,openid二选一
    logintimes = IntegerField(verbose_name='登录次数', null=True, default=0)
    updatetime = DateTimeField(verbose_name='最近登录日期', null=True, default=datetime.now())
    registtime = DateTimeField(verbose_name='注册日期', null=True, default=datetime.now())
    nick = CharField(verbose_name='显示名', max_length=128, null=True) #, unique=True
    sex = CharField(verbose_name='性别', max_length=64, null=True) 

class News(BaseModel):
    news_id = AutoField(verbose_name='编号', primary_key=True)# 定义自增
    imgsrc = CharField(verbose_name='图片', max_length=128, null=True,default='')
    title = CharField(verbose_name='标题', max_length=128, null=False,default='')
    digest = CharField(verbose_name='摘要', max_length=128, null=True,default='')
    content = CharField(verbose_name='内容', max_length=128, null=True,default='')
    froms = CharField(verbose_name='作者', max_length=128, null=True,default='')
    readcount = IntegerField(verbose_name='阅读次数', default=1) 
    datetime = DateTimeField(verbose_name='更新日期', null=True, default=datetime.now())
    
#求MD5
def MD5(src):
    import hashlib
    md5 = hashlib.md5()   
    md5.update(src)   
    return md5.hexdigest()

    
def initDB():
    if db.is_closed() :
        db.connect()
    db.create_tables([AdminUser,News])
    Init.create_table()
    inits = Init.select()
    if inits is not None and len(inits)>0:
        for init in inits:
            if init.init == 1:
                print(" DB has been init!! ")
                return
            else:
               print("initDB ??? ")
    else:
        Init.create(init =1)
        print(" initDB ok!! ")
if db.is_closed() :
    initDB()
    print("ok.")
    users = AdminUser.select()
    for user in users:
        print(user.phone+','+str(user.logintimes)+','+str(user.updatetime))
    print('users.count:'+str(users.count()))
    if users.count()<=0:
        users_dict = [
            {
              "phone": "13811001100",
              "password": MD5("654321".encode())
            },
            { 
              "phone": "13800110011",
              "password": MD5("123456".encode())
        }
        ]
        AdminUser.insert_many(users_dict).execute()
    newses = News.select().order_by(News.datetime.desc()).limit(10)
    for news in newses:
        print(str(news.news_id)+','+news.title)
    '''
    if newses.count()<=0:
        news_dict = [
            {
              "imgsrc": "",
              "title": "Python学习",
              "digest":"人生苦短，我用Python！",
              "content": "人生苦短，我用Python！Python代码量比java等语言少一个数量级",
              "froms": "陈福明",
              "readcount":2,
              "datetime": "2018-05-12 22:19",
            },
            {              
              "imgsrc": "",
              "title": "Android学习",
              "digest": "Android版本变化",
              "content": "Android版本变化比较大，Android Studio变化也比较大，现在常用的AS是3.0以上版本",
              "froms": "陈福明",
              "readcount":1,
              "datetime": "2019-05-12 22:20",
        }
        ]
    News.insert_many(news_dict).execute()
    '''
    
