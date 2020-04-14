import requests, random, datetime
from twilio.rest import Client 
from twilio.twiml.messaging_response import MessagingResponse
from settings import * # ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER, PORT, HOSTNAME

# def twilioSms(text, to):
#     client = Client(ACCOUNT_SID, AUTH_TOKEN) 
#     message = client.messages.create( 
#         from_='+12017628866',  
#         body=text,      
#         to=to 
#     ) 
#     # print(message.sid)


# def getWorldWideData():
#     url = "https:\covid-19-data.p.rapidapi.com/totals"

#     querystring = {"format":"undefined"}

#     headers = {
#         'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
#         'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
#         }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     #print(response.text)


def getDataByCountry(country_code, try_pass=False):
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

    text = smsMe(response[0])
    return text

def smsMe(response):
    country = response["country"]
    confirmed = response["confirmed"]
    recovered = response["recovered"]
    critical = response["critical"]
    deaths = response["deaths"]
    #latitude = response.["latitude"]
    #longitude = response.["longitude"]
    text = f'In {country} confirmed number of cases are {confirmed}.\n \
        Recovered people are more than {recovered}.\n \
        {critical} people are still in critical condition and {deaths} deaths'
    print(text)
    return text

def bing_news_search():
    url = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/"

    querystring = {"Category":"health"}

    headers = {
        'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "tdvwfLZVB0msh9JFhw5L074yYcoGp1UresajsnEFsmptPyHS6Z"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    body = response.json()['value']
    body = body[random.randint(0, len(body) - 1)]

    title = body["name"]
    url = body["url"]
    # image = body["image"] # thumbnail: { contentUrl, width, height}
    description = body["description"]
    provider = body["provider"] # [{ name, image: {thumbnail: { contentUrl, width, height}}}]
    news_paper_name = provider[0]['name']
    datePublished = body["datePublished"]
    date_time_obj = datetime.datetime.strptime(datePublished, '%Y-%m-%dT%H:%M:%S.%f0Z')
    # category = body["category"]
    # ampUrl = body["ampUrl"]

    text = f'*{title}*\n{description}\n\tfrom: {news_paper_name},\n\tpublished on {date_time_obj.day}-{date_time_obj.month}-{date_time_obj.year}\n{url}'
    return text