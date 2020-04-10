# Flask and Flask Extension Imports
from ..models import Doctor
from flask_jwt_extended import get_jwt_claims, get_jwt_identity

def get_doctor_dates(request):
    doctor = Doctor()
    #Get the uid from token
    doctor_id = request.args.get("did", None)
    office_id = request.args.get("oid", None)
    dates = doctor.get_dates_dict(str(office_id), str(doctor_id))
    if dates:
        response, code = {"dates": dates}, 200
    else:
        reponse, code = {"msg": "Bad doctor id"}, 400
    return response, code

def get_all_doctors():
    doctor = Doctor()
    doctors = doctor.get_doctors()
    if doctors:
        response, code = {"doctors": doctors}, 200
    else:
        response, code = {"msg": "Error retreiving doctors"}, 400
    return response, code

def get_doctors_by_office_route(request):
    doctor = Doctor()
    office_id = request.args.get("oid", None)
    doctors = doctor.get_doctors_by_office(office_id)
    if doctors:
        response, code = {"doctors": doctors}, 200
    else:
        response, code = {"msg": "Error retreiving doctors"}, 400
    return response, code

def get_doctor_data_route():
    doctor = Doctor()
    doctor_id = get_jwt_identity()['uid']
    profile = doctor.get_doctor_dict(doctor_id)
    doctor_patient = doctor.get_doctor_patient(doctor_id)
    patient_appointments = doctor.get_doctor_all_appointment(doctor_id)
    today_appointments=doctor.get_today_appointments_by_doctor(doctor_id)
    future_appointments=doctor.get_future_appts_by_doctor(doctor_id)
    past_appointments=doctor.get_past_appts_by_doctor(doctor_id),
    medication_names=doctor.get_all_medications(),
    medication_forms=doctor.get_all_medication_forms(),
    if profile:
        response, code = {"profile": profile, "patients": doctor_patient, "appointments":{"todayAppointments":today_appointments, "futureAppointments":future_appointments, "pastAppointments":past_appointments},"medications":{"medicationNames":medication_names,"medicationForms":medication_forms}}, 200
    else:
        response, code = {"msg": "Bad doctor id"}, 400
    return response, code

def get_doctor_profile_route(request):
    doctor = Doctor()
    doctor_id = request.args.get('did')
    profile = doctor.get_doctor_dict(doctor_id)
    if profile:
        response, code = {"profile": profile}, 200
    else:
        response, code = {"msg": "Bad doctor id"}, 400

    return response, code

def get_doctor_appointments_route():
    doctor = Doctor()
    doctor_id = get_jwt_identity()['uid']
    patient_appointments = doctor.get_doctor_all_appointment(doctor_id)
    today_appointments=doctor.get_today_appointments_by_doctor(doctor_id)
    future_appointments=doctor.get_future_appts_by_doctor(doctor_id)
    past_appointments=doctor.get_past_appts_by_doctor(doctor_id)

    if patient_appointments or today_appointments or future_appointments or past_appointments:
        response, code = {"appointments":{"appointments": patient_appointments,
                            "todayAppointments":today_appointments,"futureAppointments":future_appointments,
                            "pastAppointments":past_appointments}}, 200
    else:
        response, code = {"msg": "Error retrieving appointment by doctor"}, 400

    return response, code

def update_doctorprofile_route(request):
    doctor = Doctor()
    payload = request.get_json()['payload']
    doctor_id = payload['did']
    doctor_firstName = payload['dfname']
    doctor_middleInit = payload['middleInit']
    doctor_lastName = payload['dlname']
    doctor_phone = payload['phone']
    doctor_specialist = payload['specialistID']
    doctor_email = payload['email'] 
    doctor_street = payload['address']
    doctor_city = payload['city']
    doctor_state = payload['state']
    doctor_zipcode = payload['zipcode']
    doctor_race = payload['race']
    doctor_dob = payload['dob']
    doctor_gender = payload['gender']
    
    answer = doctor.update_doctor(doctor_id,doctor_firstName,doctor_middleInit, doctor_lastName,doctor_phone,doctor_specialist,doctor_email,doctor_street,doctor_city,doctor_state,doctor_zipcode,doctor_race,doctor_dob,doctor_gender)
    
    if answer:
        response, code = {"msg" : "Doctor Updated"}, 200
    else:
        response, code = {"msg": "Bad Request "}, 400

    return response, code