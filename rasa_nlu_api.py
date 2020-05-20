import requests
import logging
from common import remove_first_character


def call():
    from rasa.nlu.training_data import load_data
    from rasa.nlu import config
    from rasa.nlu.components import ComponentBuilder
    from rasa.nlu.model import Trainer

    builder = ComponentBuilder(use_cache=True)

    training_data = load_data('./rasa_folder/dataset.json')
    trainer = Trainer(config.load("./rasa_folder/config.yml"), builder)
    trainer.train(training_data)
    model_directory = trainer.persist('./rasa_folder/', fixed_model_name="models")
    print('done')
    return model_directory


def call_for(message):
    # here we want to send the message to the rasa api.

    from rasa.nlu.model import Interpreter
    interpreter = Interpreter.load('rasa_folder/models/nlu')
    parsed_sentence = interpreter.parse(message)
    return parsed_sentence


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
    if verbose is True: logging.debug("Received this JSON response from Rasa: {0}".format(response))

    # DEBUG: Received this JSON response from Rasa when I said "sad" on Discord:
    # [{'recipient_id': 'Rasa', 'text': 'Here is something to cheer you up:'},
    # {'recipient_id': 'Rasa', 'image': 'https://i.imgur.com/nGF1K8f.jpg'},
    # {'recipient_id': 'Rasa', 'text': 'Did that help you?'}]

    # TODO: Since sometimes we might receive more than one response in 1 JSON response, we would have to split them.
    response = response[0]['text']

    return response
