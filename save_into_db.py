import MySQLdb

import re
class bbsDB:
	def __init__(self):
		f = open("db.ini","r")
		pattern = re.compile(r'\w+ *: * \w+')
		pattern2 = re.compile(r' *')
		is_valid = True
		self.cursor = None
		for item in f:
			if pattern.match(item):
				st.append(item)
			elif pattern2.match(item):
				continue
			else:
				is_valid = False
		if len(st) != 3:
			is_valid = False
		if is_valid:
			self.host_name = st[0].split(':')[1]
			self.user_name = st[1].split(':')[1]
			self.user_passwd = st[1].split(':')[1]
		else:
			print 'error when match the db!please check your db.ini'
	def link_db(self):
		try:
			conn = MySQLdb.connect(host = self.host_name,root = self.user_name,passwd = self.user_passwd)
		except:
			print 'something wrong when connect the db,please check you db.ini'
		
		self.cursor = conn.cursor()
	

class Poster:
	def __init__(self):
		self.ID = ""
		self.name = ""
	def set_value(self,Id,name):
		self.Id = ID
		self.name = name
	def insert_value(self,cursor):
		values = []
		is_exit = cursor.execute("select * from poster where user_ID = " + self.ID)
		if not is_exit:
			values.append(self.ID)
			values.append(self.name)
			cursor.execute("insert into poster(user_ID,user_name) values('%s %s')",values)
		
class Post:
	def __init__(self):
		self.poster_id = 0
		self.post_time = ""
		self.post_title = ""
		self.post_content = ""
	def set_value(self,post_id,poster_id, post_time,post_title,post_content):
		self.poster_id = poster_id
		self.post_time = post_time
		self.post_title = post_title
		self.post_content = post_content
	def insert_value(self,cursor):
		values = []
		values.append(self.poster_id)
		values.append(self.post_tile)
		vlaues.append(self.post_content)
		values.append(self.post_time)
		execute_word = "insert into post(poster_id,\
				post_title,post_content,post_time) values('%d %s %s %s')"
		cursor.execute(execute_word,vlaues)	

class post_poster_relation:
	def __init__(self):
		self.postet_id = 0
		self.post_id = 0
		self.relation = 0
	def set_value(self,poster_id,post_id,relation):
		self.poster_id = poster_id
		self.post_id = post_id
		self.relation = relation

	def insert_value(self,cursor):
		values = []
		values.append(self.poster_id)
		values.append(self.post_id)
		values.append(self.relation)
		cursor.execute("insert into post_poster_relation values('%s %s %s')",values)

