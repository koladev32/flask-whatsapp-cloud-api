from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/send_message/", methods=["POST"])
def send_message():
    """_summary_: Send a message with a template to a phone number"""
    pass


@app.route("/get_message/", methods=["GET"])
def get_message():
    """__summary__: Get message from the webhook"""
    pass
