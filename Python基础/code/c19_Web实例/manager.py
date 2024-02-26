from sanic import Sanic,response
from sanic.response import *

from admin.admin import admin

app = Sanic(__name__)

from core import auth
app.config.AUTH_LOGIN_ENDPOINT = 'admin.login'
auth.setup(app)

app.blueprint(admin, url_prefix='admin') #蓝印

app.static('/static', './static') # /static
app.static('/favicon.ico', './static/b.png') # /favicon.ico 网站logo

#session
session = {}
# 存入session
@app.middleware('request')
async def add_session(request):
    request.ctx.session = session #for python3.7
    #request['session'] = session #for python3.6
#根重定向    
@app.route('/')
async def home(request):
    #print(request.ctx.session)
    #if '_auth' in request['session']:#for python3.6
    if '_auth' in request.ctx.session:#for python3.7        
        user = request.ctx.session['_auth'] #for python3.7 
        #request['session']['_auth'] #for python3.6
    return redirect('/admin/login') 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8222, debug=True)
