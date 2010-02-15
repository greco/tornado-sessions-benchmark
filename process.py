# -*- coding: utf-8 -*-

import os
import sys
import tornado
import tornado.httpserver
import tornado.web

class App(tornado.web.Application):

    def __init__(self):
        handlers = [(r'/form', FormHandler)]
        project_path = os.path.abspath(os.path.dirname(__file__))
        settings = {'cookie_secret': '6AJC6yqURMiKcY9mR8zljsp3z4fOGkeltBPmxrhyNwo=',
                    'template_path': project_path,
                    'xsrf_cookies': True,
                    'debug': False
#                    'session_storage': 'redis://',
#                    'session_storage': 'mongodb:///foo',
#                    'session_storage': 'memcached://',
#                    'session_storage': 'mysql://root:root/foo',
#                    'session_storage': 'dir://',
                    }
        tornado.web.Application.__init__(self, handlers, **settings)

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        # uncomment the following line when using sessions        
        # self.session['color'] = self.get_argument('color')
        self.redirect('/')

if __name__ == '__main__':
    port = int(sys.argv[1])
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
