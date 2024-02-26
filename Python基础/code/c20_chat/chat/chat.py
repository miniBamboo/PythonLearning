#通用聊天室
'''
使用方法：(主文件中)
from  chat.chat import chat
app.blueprint(chat, url_prefix='chat')
'''
import os,json,random
from datetime import datetime
from sanic import Blueprint, response
from sanic.response import redirect,text,html,file,json
from jinja2 import Environment, PackageLoader, select_autoescape

chat = Blueprint('chat')
env = Environment(
    loader=PackageLoader('chat', './templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))

#网页渲染
def template(tpl, **kwargs):
    templater = env.get_template(tpl)
    return html(templater.render(kwargs))
#root
@chat.route('/')
#@auth.login_required
async def index(request):
    print('/chat')
    return template('chat.html')
#主页
@chat.route('/index')
async def index(request):
    print('/chat/index ')
    return template('chat.html')

#聊天室全局变量
wslist = []
wsnames = []
#进入聊天室
def in_chat(ws,name):
    wslist.append(ws)
    wsnames.append(name)
#退出聊天室
def out_chat(ws,name):
    wslist.remove(ws)
    wsnames.remove(name) 
#-----------------路由开始----------------------------
wslist = []
@chat.websocket('/ws/<name>')
async def do_chat(request,ws,name): 
    global wslist
    global wsnames 
    retstr='{"from_user":"系统","to_user":"所有人","chat":"'+name+'登录了."}'
    for wss in wslist:
        await wss.send(retstr)
    in_chat(ws,name)    
    try:
        while True:            
            data = await ws.recv()
            print('Received: ' + data) 
            if "在线用户"== data:
                data = ' {"from_user":"在线用户","to_user":"在线用户","chat":" ' +str(wsnames)+' "} '
                print('Sending: ' + data)
                await ws.send(data)
                continue            
            for wss in wslist:
                if ws != wss:
                    await wss.send(data) 
        out_chat(ws,name)
        retstr='{"from_user":"系统","to_user":"所有人","chat":"'+name+'已退出."}'
        print(retstr)
        for wss in  wslist:            
            await wss.send(retstr)
    except Exception as e:
        print(e) 
        out_chat(ws,name)
        retstr='{"from_user":"系统","to_user":"所有人","chat":"'+name+'已退出."}'
        print(retstr)
        for wss in wslist:            
            await wss.send(retstr)
