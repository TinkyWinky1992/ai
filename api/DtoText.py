

def doctorMessage(messageDoctor: str):
    return {'message': messageDoctor}


def appointmentMessage(level, typeOfProblem, username, email, id) -> dict:
    return {
        'username': username,
        'email': email,
        'level': level,
        'problem': typeOfProblem,
        'id': id
    }

