import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from utils.utils import Utils

import hashlib
from conf.webConf import Handlers
from app.SecureHandler import SecureHandler
import conf.baseConf

'''
class Ttt(tornado.web.RequestHandler):
	def get(self, ppp):
		print("get",ppp)
		self.write("get \n")
	def post(self, ppp):
		print("post",ppp)
		self.write("post \n")
'''

class Application(tornado.web.Application): 
	def __init__(self):
		handlers = Handlers().commonHandlers 
		s = (r"/sec/(\S+)", SecureHandler)
		handlers.append(s)
		print(handlers)
		settings = dict(
			template_path = conf.baseConf.TemplatePath,
			static_path= conf.baseConf.StaticPath,
			cookie_secret = Utils.gen64uuid(), #app invalid?
			xsrf_cookies = True,
			login_url = "/index",
			#debug=True,
		)
		print("settings cookie_secre", settings["cookie_secret"])
		tornado.web.Application.__init__(self, handlers, **settings)	
        
