from app.DB import DB 

class UserModel:
	def __init__(self, uname, pwd):	
		self.uname = uname	
		self.pwd = pwd

	def getUname(self):
		return self.uname

