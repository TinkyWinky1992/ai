import os
from api.server import getAppointment


def save_schedule(problem, level):
    getAppointment(level, problem)
    return "appointment saved"


