# appointment.py
from flask import jsonify
from api.DtoText import appointmentMessage
import requests
from utils import TakeUserDetails
url = "http://localhost:5000/queue/create"


def getAppointment(level, problem):
    user_profile: dict = TakeUserDetails()
    appointment = appointmentMessage(level, problem, user_profile['username'], user_profile['email'])
    response = requests.post(url, json=appointment)
    print(response)





