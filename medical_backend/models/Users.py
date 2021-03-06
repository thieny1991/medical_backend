from bcrypt import checkpw, gensalt, hashpw
from ..database import Database

db = Database()

class User:

	def check_reg_user(self, email):
		sql = "SELECT * FROM `users` WHERE email=%s"
		params = (email)
		result = db.run_query(sql, params)
		return result

	def check_reg_doctor(self, email):
		sql = "SELECT * FROM `doctors` WHERE email=%s"
		params = (email)
		result = db.run_query(sql, params)
		return result

	def check_auth_user(self, email):
		sql = "SELECT * FROM `users` WHERE email=%s"
		params = (email)
		result = db.run_query(sql, params)
		return result[0]

	def check_password(self, email, password):
		sql = "SELECT `password` FROM `users` WHERE email=%s"
		params = (email)
		result = db.run_query(sql, params)
		password_hash = result[0]['password'].encode('utf-8')
		return checkpw(password.encode('utf-8'), password_hash)

	def add_user(self, email, password, role_id, user_id,today):
		hashed = hashpw(password.encode('utf-8'), gensalt(14))
		sql = "INSERT INTO `users` (`id`, `email`, `password`, `role_id`, `user_role_id`,`date_account_created`) VALUES (NULL, %s, %s, %s, %s,%s)"
		params = (email,hashed,role_id,user_id,today)
		db.run_query(sql, params)