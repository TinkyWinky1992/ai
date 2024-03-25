

def doctorMessage(messageDoctor: str):
    return {'message': messageDoctor}


def appointmentMessage(level, typeOfProblem, username, email) -> dict:
    return {
        'username': username,
        'email': email,
        'level': level,
        'problem': typeOfProblem,
    }
