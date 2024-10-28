import requests
# Made with https://opentdb.com/

parameters = {
    "amount": 10,
    "category": 15,
    "type": "boolean",
}

respond = requests.get("https://opentdb.com/api.php", params=parameters)
respond.raise_for_status()
data = respond.json()
question_data = data["results"]
