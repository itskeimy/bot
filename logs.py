import sqlite3

class logins:
	def __init__(self, database_file):
		self.connection = sqlite3.connect(database_file, check_same_thread=False)
		self.cursor = self.connection.cursor()
	def check_user(self, login, password):
		with self.connection:
			self.cursor.execute(f"SELECT logins FROM users WHERE logins = '{login}'")
			if self.cursor.fetchone() is None:
				return 0
			else:
				self.cursor.execute(f"SELECT password FROM users WHERE logins = '{login}'")
				if self.cursor.fetchone()[0] == password: 
					return 1
				else:	
					return 0
	def add_user(self, login, password):
		with self.connection:
			self.cursor.execute(f"INSERT INTO users VALUES (?, ?)", (login, password))
			self.connection.commit()						
