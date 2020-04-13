import requests, os, threading
from twilio.rest import Client 
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from settings import ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER, PORT, HOSTNAME

def twilioSms(text, to):
    client = Client(ACCOUNT_SID, AUTH_TOKEN) 
    message = client.messages.create( 
        from_='+12017628866',  
        body=text,      
        to=to 
    ) 
    # print(message.sid)


def getWorldWideData():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    querystring = {"format":"undefined"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)


def getDataByCountry(country_code, to, try_pass=False):
    if try_pass:
        url_country, qr = "https://covid-19-data.p.rapidapi.com/country", "name"
    elif len(country_code) < 3:
        url_country, qr = "https://covid-19-data.p.rapidapi.com/country/code", "code"
    else:
        url_country, qr = "https://covid-19-data.p.rapidapi.com/country", "name"

    querystring = {"format":"undefined",qr:country_code}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
        }

    response = requests.request("GET", url_country, headers=headers, params=querystring)
    response = response.json()
    if len(response) < 1:
        if try_pass == False:
            return getDataByCountry(country_code, True)
        else:
            raise IndexError

    return smsMe(response[0], to)

def smsMe(response, to):
    country = response["country"]
    confirmed = response["confirmed"]
    recovered = response["recovered"]
    critical = response["critical"]
    deaths = response["deaths"]
    #latitude = response.["latitude"]
    #longitude = response.["longitude"]
    text = f'in {country} confirmed number of cases are {confirmed}\nRecovered people are more than {recovered}.\nAlthough there are {critical} people are in critical candition and {deaths} deaths'
    return twilioSms(text, to)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def reply_country_info():
    """Respond to incoming messages with a friendly SMS. :)"""
    # Start our response
    resp = MessagingResponse()
    body = request.values.get("Body")
    to = request.values.get("From")

    try:
        body = getDataByCountry(body, to)
    except IndexError:
        resp.message("No such country found, check your spelling and try again")
        return str(resp)

    resp.message(body, to)
    return str(resp)

if __name__ == "__main__":
    t1 = threading.Thread(target=os.system, args=(f'twilio phone-numbers:update {PHONE_NUMBER} --sms-url="http://{HOSTNAME}:{PORT}/sms"',))
    t2 = threading.Thread(target=app.run)
    t1.start()
    t2.start()

    # app.run(debug=True, threaded=True)
    # os.system(f'twilio phone-numbers:update {PHONE_NUMBER} --sms-url="http://{HOSTNAME}:{PORT}/sms"')

