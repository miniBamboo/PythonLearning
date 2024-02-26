from sanic import Sanic,response
from sanic.response import *

from chat.chat import chat

app = Sanic(__name__)

app.blueprint(chat, url_prefix='chat')

app.static('/static', './static')
app.static('/favicon.ico','./static/png/favicon.png')

@app.route('/')
async def home(request):
    return redirect('/chat') 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8088, debug=True)
