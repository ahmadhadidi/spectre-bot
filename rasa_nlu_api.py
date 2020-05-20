import requests
import logging
from common import remove_first_character

def query_rasa(message, verbose):
    # We bind the URL of the Rasa Sanic server.
    URL = "http://localhost:5005/webhooks/rest/webhook"

    # We remove the '!' from the message
    message = remove_first_character(message, True)

    # We prepare a JSON object that contains the discord message.
    data = {
        "sender": "Rasa",
        "message": message
    }

    # We add this necessary header to the request object that we want to POST
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    # We send the request as a POST.
    r = requests.post(url=URL, json=data, headers=headers)

    # We save the response of Rasa as a JSON object in the variable response.
    response = r.json()

    # For debugging purposes, we can look what is inside the response coming from Rasa.
    if verbose is True: print("Received this JSON response from Rasa: {0}".format(response))

    # DEBUG: Received this JSON response from Rasa when I said "sad" on Discord:
    # [{'recipient_id': 'Rasa', 'text': 'Here is something to cheer you up:'},
    # {'recipient_id': 'Rasa', 'image': 'https://i.imgur.com/nGF1K8f.jpg'},
    # {'recipient_id': 'Rasa', 'text': 'Did that help you?'}]

    # TODO: Since sometimes we might receive more than one response 
    # in 1 JSON response, we would have to split them.
    response = response[0]['text']

    return response
