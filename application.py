from flask import Flask, request
import sys
import os 
import ssl

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/lib')

import slack

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

app = Flask(__name__)


@app.route("/sendMessage", methods=["POST"])
def hello():
    ACCESS_TOKEN = request.headers.get("Authorization").replace('Bearer ','')
    client = slack.WebClient(token=ACCESS_TOKEN,ssl=ssl_context)
    channel_id = "CSA3YU1S6"
    message = request.get_json(force=True).get("message")
    client.chat_postMessage(channel=channel_id, text=message)
    return 'OK'