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

## Train the Chatbot
``` sh
rasa train
```

## My Discord Webhook
``` sh
https://discordapp.com/api/webhooks/704434829978239018/a6AKQJprSQ6qbdP07A0tJJdYT0GHgqWVSAPTFkQ0CU1SUO5IDE9vOk2Gcrz-skwlydvO

Channel: #general
```

## My Discord Token
``` shell script
NzAzNDA1MjU3MDgyMDExNjcw.XqtJIA.QOzgLwTxL1_ES04o8z5EWU9Y5Nw
```

## Run the Chatbot
``` sh
rasa run -m models --enable-api --cors "*" --debug
```

# Journal

* Hopefully, we can connect to discord by 
following [this](https://forum.rasa.com/t/solved-how-to-implement-our-own-custom-connector-for-the-custom-ui/12675) 
guide. Maybe we can connect to discord via the custom connector concept.
C:\dev\rasa_test4\rasa_folder\models\nlu