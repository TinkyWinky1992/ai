import urllib
from mailbox import Message
from flask_cors import CORS
from flask import Flask, jsonify
from api.DtoText import doctorMessage
from Doctor import Roberto
from flask import request
from utils import profileFile
app = Flask(__name__)
CORS(app)
roberto_ai = Roberto()


@app.route("/", methods=['GET'])
async def startConversation():

    profileFile(request.args.get('username'), request.args.get('email'), request.args.get('id'))
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
        print("dict", doctorMessage_dict)
        return jsonify(doctorMessage_dict)

    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500  # Internal server error


if __name__ == '__main__':
    print("Starting Server...")
    app.run(host='0.0.0.0', port=5001)
