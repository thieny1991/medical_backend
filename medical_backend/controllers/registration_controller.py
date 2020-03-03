from flask_jwt_extended import create_access_token
from ..models import Patient, User

def registration_route(request):
	patient = Patient()
	user = User()
	req_email = request.json.get("email", None)
	if user.check_user(req_email):
		response, code = {"msg": "Email already exists!"}, 401
	else:
		uid = patient.add_patient(request)
		user_id = {"uid":uid,"role":2}
		response, code = {"access_token": create_access_token(user_id)}, 201
	return response, code