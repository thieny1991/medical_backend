# Flask and Flask Extension Imports
from ..models import Doctor

def get_doctor_dates(request):
	doctor = Doctor()
	#Get the uid from token
	doctor_id = request.args.get("doctor_id", None)
	dates = doctor.get_dates_dict(doctor_id)
	if dates:
		response, code = {"dates": dates}, 200
	else:
		reponse, code = {"msg":"Bad doctor id"}, 400

	return response, code