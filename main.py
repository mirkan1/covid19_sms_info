import os, threading
from flask import Flask, request, session
from settings import *
from assets import *

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def reply_country_info():
    """Respond to incoming messages with a friendly SMS. :)"""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get("Body")
    to = request.values.get("From")

    # IF MESSAGE IS NEWS
    if body == "news":
        body = bing_news_search()
        resp.message(body)
        return str(resp)

    # IF MESSAGE IS COUNTRY_CODE
    try:
        body = getDataByCountry(body)
    except IndexError:
        resp.message("No such country found, check your spelling and try again")
        return str(resp)

    resp.message(body)
    return str(resp)

if __name__ == "__main__":
    t1 = threading.Thread(target=os.system, 
        args=(f'twilio phone-numbers:update {PHONE_NUMBER} --sms-url="http://{HOSTNAME}:{PORT}/sms"',)
    )
    t2 = threading.Thread(target=app.run)
    t1.start()
    t2.start()