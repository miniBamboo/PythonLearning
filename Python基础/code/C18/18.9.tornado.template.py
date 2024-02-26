import tornado.ioloop
import tornado.web  
class MainHandler(tornado.web.RequestHandler):
    def get(self): 
        items = ["Item 1", "Item 2", "Item 3"]
        self.render('home/index.html', title="My title", items=items)
  
settings = {
    'template_path': 'template',
}
  
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)  
  
if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

