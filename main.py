import requests
from twilio.rest import Client 
 


def twilioSms():
    astest = "ACcb3d6464eeee7a1fadbb9d220a9ca426"
    attest = "cd3393bbaec2eb494e39c5828973e8ee"
    account_sid = 'AC5dfb129606b1c1a1bb34683ac40f9192' 
    auth_token = 'daa8b1b9f4dd4c123eeac9eabab04ea4' 

    client = Client(account_sid, auth_token) 
    #client = Client(astest, attest)

    message = client.messages.create( 
                                from_='+12017628866',  
                                body='hello again this is Mirkan',      
                                to='+15044324114' 
                            ) 
    print(message.sid)


def getWorldWideData():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    querystring = {"format":"undefined"}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def getDataByCountry(country_code="tr"):
    url_country_code = "https://covid-19-data.p.rapidapi.com/country/code"
    url_country_name = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"format":"undefined","code":country_code}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
        }

    response = requests.request("GET", url_country_code, headers=headers, params=querystring)

    print(response.text)

getDataByCountry("usa")