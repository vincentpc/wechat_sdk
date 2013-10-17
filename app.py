# -*- coding: utf-8 -*-

import tornado.web
from handlers.wechat import WeChat
from handlers.processxml import processXml

class YixinHandler(tornado.web.RequestHandler):
    def get(self):
        try:

            if WeChat.valid(self.get_argument('signature'),
                        self.get_argument('nonce'),
                        self.get_argument('timestamp')):
                self.write(self.get_argument('echostr'))
        except tornado.web.HTTPError:
            self.write('')
    
    def post(self):
        try:
            if WeChat.valid(self.get_argument('signature'),
                        self.get_argument('timestamp'),
                        self.get_argument('nonce')):
                data = processXml(self.request.body)
                self.set_header("Content-Type", "application/xml; charset=UTF-8")
                self.write(data)
        except tornado.web.HTTPError:
            self.write('')


application = tornado.web.Application([
    (r"/yixinpublic", YixinHandler),
   # (r"/wechatpublic", WechatHandler),
    (r"/", tornado.web.RedirectHandler, dict(url="vincentpc.github.com")),
], debug=True)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
