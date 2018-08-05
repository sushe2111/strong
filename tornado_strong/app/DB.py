import pymysql
from conf.baseConf import DatabaseConf 

# 打开数据库连接

class DB:
	#字典
	cursor_type = pymysql.cursors.DictCursor
	def __init__(self):
		self.conn = pymysql.connect(DatabaseConf["host"] ,DatabaseConf["user"], DatabaseConf["password"], DatabaseConf["dbName"] )
	
	def escape(self, param):
		param = self.conn.escape_string(param)
		return param

	def query(self, sql):
		conn = self.conn
		cursor = conn.cursor(self.cursor_type)
		
		cursor.execute(sql);
		result = cursor.fetchall()
		print(result)
		return result

	def queryEscape(self, sql):
		sql = self.conn.escape_string(sql)
		result = self.query(sql)
		return result 

	def update(self, sql):
		pass

	def insert(self, sql):
		pass

	def insertmany(self, sql, data):
		pass

#db连接池
class DBPool:
	pass
		
