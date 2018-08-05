import tornado.web

import hashlib
from conf.webConf import Handlers

S2Uids = {}

#test
AutoIndex = 9899

SecureHandlersDict = Handlers.secureHandlers

class SecureHandler(tornado.web.RequestHandler):

	def get_current_user(self):
		return self.get_secure_cookie("sessionid")

	@tornado.web.authenticated
	def post(self, name):
		print(" secure",name)
		if name in SecureHandlersDict:
			sessionid = self.get_secure_cookie("sessionid", None) #self.get_argument('sessionid')
			if sessionid is None: 
				#self.render('login.html')
				self.write("none session \n")	
				return
			
			uid = self.get_argument('uid')
			if S2Cids[sessionid] != uid:		
				#self.render('login.html')
				self.write("session error \n")	
				return
			
			handle = SecureHandlersDict[name](self)
			handle.post(self)
					
			self.write("ok\n")	
			return


	@tornado.web.authenticated
	def get(self, name):
		print("sec get",name)
		self.write(" need post \n")
