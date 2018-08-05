from app.controller.BaseHandler import BaseHandler
from app.db.user import UserDB
import hashlib

class LoginHandler(BaseHandler):
	def post(self):
	
		uname = self.get_argument('uname')
		pwd = self.get_argument('pwd') #md5
		if not UserDB.checkUser(uname, pwd):
			self.m_response(1, msg="uname or password error")
			return

		uid = UserDB.getUidByUname(uname)
		self.set_secure_cookie("sessionid", str(uid),0) # third param is expire days	

		self.m_response(0,{"uname":uname})
		return

