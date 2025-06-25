import logging

import flask
from flask import request



logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger("app")

app = flask.Flask(__name__)

@app.route("/consumeWebhook", methods=['Post'])
def consume_Webhook():
   body = request.get_json()

   _LOGGER.info("Recieved Webhook: %s", body)

   return flask.Response(status=200)

if __name__ == "__main__":
   app.run()
   
    

