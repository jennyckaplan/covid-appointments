import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

def appointments_are_available():
    url = 'https://www.lifespan.org/centers-services/coronavirus-covid-19/lifespan-covid-19-vaccination-program/schedule-vaccine'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    no_appointments = soup(text=lambda t: "No appointments are currently available" in t)
    if len(no_appointments) == 0:
        return True
    return False

while True:
    dt = datetime.now()
    curr_seconds = dt.second
    if (curr_seconds % 60 == 0):
        are_appointments = appointments_are_available()
        if (are_appointments):
            message = client.messages.create(
                to="+1<your-phone-number>", 
                from_="+1<your-twilio-number>",
                body="OH YEAH!! Go get that appointment!! https://www.lifespan.org/centers-services/coronavirus-covid-19/lifespan-covid-19-vaccination-program/schedule-vaccine")
        time.sleep(1)
