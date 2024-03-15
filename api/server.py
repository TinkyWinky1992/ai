from flask import Flask, jsonify
from api.DtoText import appointmentMessage, doctorMessage
import sys
from Doctor import Roberto

sys.path.append("/path/to/directory/containing/Dto.py")
app = Flask(__name__)
roberto_ai = Roberto()


@app.route("/", method=['GET'])
def startConversation():
    roberto_ai.startNewConversation()


@app.route("/postMessage", methods=['POST'])
def postMessage():
    print("hi")
    return jsonify("Hi")


@app.route("/getMessage", methods=['GET'])
def sendMessage(messageDoctor):
    with app.app_context():
        Message = doctorMessage(messageDoctor)
        print(Message)
        return jsonify(Message)


@app.route("/getAppointment", methods=['GET'])
def getAppointment(level: int, problem: str):
    with app.app_context():
        appointment = appointmentMessage(level, problem)
        return jsonify(appointment)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
