

def doctorMessage(messageDoctor: str):
    return {'message': messageDoctor}


def appointmentMessage(level: int, typeOfProblem: str):
    return {
        'level': level,
        'problem': typeOfProblem
    }
