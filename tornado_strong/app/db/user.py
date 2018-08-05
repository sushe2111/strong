from app.DB import DB

class UserDB:
	def checkUser(uname, pwd):
		print("check user", uname, pwd)
		if (uname is None) or (pwd is None):
			return False

		conn = DB()
		uname = conn.escape(uname)  
		pwd = conn.escape(pwd)  
		rows = DB().query("SELECT * FROM User WHERE uname='%s' AND password='%s'" % (uname, pwd) )
		if len(rows)<1:
			return False

		uid = rows[0]['uid']
		
		if uid is None:
			return False

		return True

	def getUidByUname(uname):
		if (uname is None) :
			return None 

		conn = DB()
		uname = conn.escape(uname)  

		rows = conn.query("SELECT * FROM User WHERE uname='%s' " % (uname) )
		if len(rows)<1:
			return None 

		return rows[0]['uid']

