import os
cfgdir = os.path.abspath(os.path.dirname(__file__))
TESTING = True

# 数据库配置
#MySQL:
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWORD = '123456'
db_setting = {
    'host': HOST,
    'port': PORT,
    'password': PASSWORD,
    'user': USER
}
MYSQL_DB_NAME = 'web_admin'
#sqlite:
SQLITE_FILE_DIR = os.path.join( cfgdir,'db')
SQLITE_FILE = 'web_admin.sqlite'


