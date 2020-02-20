from bcrypt import checkpw, gensalt, hashpw
from ..database import Database
from ..models import User

db = Database()
cur = db.cur

class Client(User):

	def add_client(self, request):
		req_first_name = request.json.get("firstName", None)
		req_middle_i = request.json.get("middleInit", None)
		req_last_name = request.json.get("lastName", None)
		req_street_1 = request.json.get("street", None)
		req_city = request.json.get("city", None)
		req_state = request.json.get("state", None)
		req_zipcode = request.json.get("zipcode", None)
		req_phone = request.json.get("phone", None)
		req_dob = request.json.get("dob", None)
		req_gender = request.json.get("gender", None)
		req_marital = request.json.get("marital", None)
		req_race = request.json.get("race", None)
		req_email = request.json.get("email", None)
		sql = "INSERT INTO `clients` (`client_id`, `first_name`, `middle_initial`, `last_name`, `street_1`, `city`, `state`, `zipcode`, `phone`, `date_of_birth`, `gender`, `marital_status`, `race`, `email`, `primary_doctor`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL)"
		params = (str(req_first_name),str(req_middle_i),str(req_last_name),str(req_street_1),str(req_city),str(req_state),str(req_zipcode),str(req_phone),str(req_dob),str(req_gender),str(req_marital),str(req_race),str(req_email))
		cur.execute(sql, params)
		cur.execute("SELECT `client_id` FROM `clients` ORDER BY `client_id` DESC LIMIT 1")
		result = cur.fetchone()
		uid = result['client_id']
		self.add_user(req_email, request.json.get("password", None), 2, uid)
		return uid

	def update_client(self, r, client_id):
		sql = "UPDATE clients SET first_name=%s, middle_initial=%s, last_name=%s, street_1=%s, city=%s, state=%s, zipcode=%s, phone=%s, date_of_birth=%s, gender=%s, marital_status=%s, race=%s, email=%s WHERE client_id=%s"
		params = (str(r.form['first_name']),str(r.form['middle_initial']),str(r.form['last_name']),str(r.form['street_1']),str(r.form['city']),str(r.form['state']),str(r.form['zipcode']),str(r.form['phone']),str(r.form['dob']),str(r.form['gender']),str(r.form['marital_status']),str(r.form['race']),str(r.form['email']),client_id)
		cur.execute(sql, params)

	def get_client_dict(self, client_id):
		sql = "SELECT * FROM `clients` WHERE client_id=%s"
		params = (client_id,)
		cur.execute(sql, params)
		result = cur.fetchone()
		profile = {
			"firstName": result['first_name'],
			"middleInit": result['middle_initial'],
			"lastName": result['last_name'],
			"street": result['street_1'],
			"city": result['city'],
			"state": result['state'],
			"zipcode": result['zipcode'],
			"phone": result['phone'],
			"dob": result['date_of_birth'],
			"gender": result['gender'],
			"marital": result['marital_status'],
			"race": result['race']
		}
		return profile