from bcrypt import checkpw, gensalt, hashpw
from ..database import Database

db = Database()
cur = db.cur

class User:

	def check_user(self, email):
		sql = "SELECT * FROM `users` WHERE email=%s"
		params = (email)
		cur.execute(sql, params)
		result = cur.fetchone()
		return result

	def check_password(self, email, password):
		sql = "SELECT * FROM `users` WHERE email=%s"
		params = (email)
		cur.execute(sql, params)
		result = cur.fetchone()
		password_hash = result['password'].encode('utf-8')
		return checkpw(password.encode('utf-8'), password_hash)

	def add_user(self, email, password, role_id, user_id):
		hashed = hashpw(password.encode('utf-8'), gensalt(14))
		sql = "INSERT INTO `users` (`id`, `email`, `password`, `role_id`, `user_role_id`) VALUES (NULL, %s, %s, %s, %s)"
		params = (email,hashed,role_id,user_id)
		cur.execute(sql, params)