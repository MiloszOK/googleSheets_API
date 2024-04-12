import requests
import datetime
import os

WEIGHT = 78
HEIGHT = 186
AGE = 21

EXCERCISE = input('Powiedz, jakie ćwiczenia dzisiaj wykonywałeś: ')

header = {
    'x-app-id' : os.environ.get('EV_API_ID'),
    'x-app-key' : os.environ.get('EV_API_KEY'),
}

query = {
    'query': EXCERCISE,
    'weight_kg' : WEIGHT,
    'height_cm' : HEIGHT,
    'age' : AGE,
}

response = requests.post(url=os.environ.get('EV_URL'), headers=header, json=query)
response.raise_for_status()
execcc = response.json()


date = datetime.datetime.now()

header2 = {
    'Authorization' : os.environ.get('EV_AUT')
}


for activities in execcc["exercises"]:
    workout = {
        'workout' : {
            'date' : f'{date.strftime("%d/%m/%Y")}',
            'time' : f'{date.strftime("%H:%M:%S")}',
            'exercise' : f'{activities["user_input"].title()}',
            'duration' : f'{activities["duration_min"]}',
            'calories' : f'{activities["nf_calories"]}',
        }
    }

    excercise = requests.post(url=os.environ.get('EV_URL_SHEET'), headers=header2, json=workout)
