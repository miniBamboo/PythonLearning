import os,json,requests
from datetime import datetime

from sanic import Blueprint, response
from sanic.response import redirect,text,html,file,json
from jinja2 import Environment, PackageLoader, select_autoescape

from core import auth
from sanic_auth import Auth,User

from  model.models import *
import config as cfg


admin = Blueprint('admin')
admin.static('/static', './static') # /admin/static
admin.static('/favicon.ico', './static/b.png') # /admin/favicon.ico

env = Environment(
    loader=PackageLoader('admin', '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))

    

#网页渲染
def template(tpl, **kwargs):
    templater = env.get_template(tpl)
    return html(templater.render(kwargs))
#求MD5
def MD5(src):
    import hashlib
    md5 = hashlib.md5()   
    md5.update(src)   
    return md5.hexdigest()
#登录
@admin.route('/login',methods=['GET', 'POST']) #/<phone>/<password>
async def login(request):    
    print('/admin/login')
    if request.method == 'GET':
        return template('login.html',error="请输入用户名或者密码")    
    phone = request.form.get('username')
    password = request.form.get('password')
    print(phone,password)
    
    md5 = MD5(password.encode("utf8"))
    users=None
    try:
        #step 1
        users = AdminUser.select().where(AdminUser.phone == phone)
        #step 2  
        if users.count()>=1: 
            baseuser=users.get()
            if baseuser.password != md5:
                print(baseuser.password+':'+md5+" is not equal.")
                return template('login.html',error="请输入正确的密码")
            user = User(id=baseuser.phone,name=baseuser.password)
            auth.login_user(request,user)
            #return redirect('/admin/news/admin')
            return template('index.html')
        else:
            return template('login.html',error="用户名不正确")
    except Exception as e:
        return template('login.html',error="用户名或密码不正确")
@admin.route('/logout')
@auth.login_required
async def logout(request):
    print('/admin/logout')
    auth.logout_user(request)
    return template('logout.html')#,error="已经退出，请重新登录系统"
#root
@admin.route('/')
#@auth.login_required
async def index(request):
    print('/admin')
    return redirect('/admin/login')
#主页
@admin.route('/index')
@auth.login_required
async def index(request):
    print('/admin/index ')
    return template('index.html')
#添加新闻
@admin.route('/news/admin',methods=['GET','POST']) # 
@auth.login_required
async def add_news(request):
    print('/admin/news/admin')
    if request.method == 'GET':
        return template('newsadd.html')  
    title = request.form.get('title')
    digest = request.form.get('digest')
    imgsrc = request.form.get('imgsrc') #''
    if not imgsrc:
        imgsrc = ''
    content = request.form.get('content')
    froms = request.form.get('froms')
    if (not title)  or len(title)==0:
        return template('newsadd.html',error="新闻空错误")
    news = News.create(title=title,digest=digest,imgsrc=imgsrc,content=content,froms=froms )
    if not news:
        return template('newsadd.html',error="新闻插入错误")
    else:
        return template('newsadd.html',error="新闻插入成功!!")
#获取最近10条新闻
@admin.route('/news/get',methods=['GET', 'POST'])
@auth.login_required
async def get_news(request):
    print('/admin/news/get')
    newses = News.select().order_by(News.datetime.desc()).limit(10)
    #for news in newses:
    if  newses.count()>=0:
        return template('newsget.html',cates=locals())
    else:
        return template('index.html',error="新闻没用找到!!")
#获取新闻详情
@admin.route('/news/detail',methods=['GET', 'POST'])
async def get_news_detail(request):
    if request.method == 'GET':
        return redirect('/admin/news/get')
    num = request.form.get('newsid')
    print('/admin/news/detail/'+num)
    try:
        newsid = int(num)
        id_newses = News.select().where(News.news_id == newsid)
        if  id_newses.count()>=0:
            onenews = id_newses.get()
            readcount = onenews.readcount + 1
            ns = News.update(readcount=readcount).where(News.news_id == newsid).execute()
            #print('To template',readcount,onenews.readcount)
            print(onenews)
            #newses = News.select().where(News.news_id == newsid)
            return template('newsdetail.html',news=onenews)
        else:
            print(u'没有该新闻,id:'+num)
            return template('index.html',error="新闻没用找到!!,新闻id:"+num)
    except Exception as e:
        return template('index.html',error="新闻异常:"+str(e))
#删除新闻详情
@admin.route('/news/del',methods=['GET', 'POST'])
@auth.login_required
async def del_news(request):
    if request.method == 'GET':
        return redirect('/admin/news/get')
    num = request.form.get('newsid')
    print('/admin/news/del/'+num)
    try:
        newsid = int(num)
        news = News.delete().where(News.news_id == newsid).execute()
        #print(news)
        return redirect('/admin/news/get')
        '''if  not news:
            return redirect('/admin/news/get')
        else:
            print(u'没有该新闻,id:'+num)
            return template('index.html',error="删除新闻异常，新闻没用找到!! 新闻id:"+num)'''
    except Exception as e:
        return template('index.html',error="删除新闻异常:"+str(e))
#获取User
@admin.route('/user/get',methods=['GET', 'POST'])
@auth.login_required
async def get_users(request):
    print('/admin/user/get')
    users = AdminUser.select() #.where(AdminUser.phone == phone)
    if  users.count()>=0:
        return template('showusers.html',cates=locals())
    else:
        return template('index.html',error="用户没用找到!!")
#日志查看
already_print_num = 0
@admin.route('/logs/get',methods=['GET', 'POST'])
@auth.login_required
def get_rank2_logs(request):
    global already_print_num
    import  os
    filepath = '/tmp/web_admin.log'
    if not os.path.exists(filepath):
        return template('showlog.html',error='no such file %s' % filepath) 
    readfile = open(filepath, 'r')
    lines = readfile.readlines()
    readfile.close()
    if len(lines) > 20 and already_print_num == 0:
        #last_num = 20  #首次输出最多输出20行
        #经nonoob指正，修改如下
        already_print_num = len(lines) - 20
    if already_print_num < len(lines):
        print_lines = lines[already_print_num-len(lines):]#len(lines) -        
        already_print_num = len(lines)
        return template('showlog.html',logs=print_lines) 
    return template('showlog.html',error='已经读取计数异常')
