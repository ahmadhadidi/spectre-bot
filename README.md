## Prerequisites

* Python 3.7.5

## Run The Virtual Environment

``` sh
.\venv\Scripts\activate
```

## Download Dependencies (After Activating the virtual environment)

``` sh
pip install -r requirements.txt
```

## Discord Token

Obtain it [here](https://discord.com/developers/applications) by creating an application
and declaring that it is a bot. Refer to the numerous guides on how to do that online.

## Run Rasa for the Chatbot

This python file checks whether if training is needed for Rasa 
and then launches its server.

``` sh
python .\rasa_folder\run_rasa.py
```

## Available Commands

* `-weather cologne`
* `-corona belgium`
* `-fuel`
* `-news`
* `!are you a bot?`
