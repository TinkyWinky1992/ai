import urllib
from mailbox import Message
from flask_cors import CORS
from flask import Flask, jsonify
from api.DtoText import appointmentMessage, doctorMessage
from Doctor import Roberto
from appointment import getAppointment  # Importing getAppointment function from appointment.py
from flask import request
app = Flask(__name__)
CORS(app)
roberto_ai = Roberto()


@app.route("/", methods=['GET'])
async def startConversation():
    roberto_ai.startNewConversation()
    return jsonify("True")


@app.route("/getMessage", methods=['GET'])
async def sendMessage():
    try:
        # Retrieve and validate the 'messageToDoctor' parameter
        messageToDoctor = request.args.get('messageToDoctor')
        # Decode the message (assuming it was encoded on the client-side)
        messageToDoctor = urllib.parse.unquote(messageToDoctor)
        message = roberto_ai.ConversationPerMessage(messageToDoctor)
        print(message)
        doctorMessage_dict = doctorMessage(message)
        return jsonify(doctorMessage_dict)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500  # Internal server error


app.route("/getAppointment", methods=['GET'])(getAppointment)

if __name__ == '__main__':
    print("Starting Server...")
    app.run(host='0.0.0.0', port=5001)
