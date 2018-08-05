import tornado.web
import json

class BaseHandler(tornado.web.RequestHandler):
	def m_response(self, retcode, data=None, msg=None):	
		self.write( dict(code=retcode, data=data, msg=msg) )
		
	
		
		
