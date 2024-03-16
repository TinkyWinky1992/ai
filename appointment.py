# appointment.py
from flask import jsonify
from api.DtoText import appointmentMessage


async def getAppointment(level: int, problem: str):
    appointment = appointmentMessage(level, problem)
    return jsonify(appointment)
