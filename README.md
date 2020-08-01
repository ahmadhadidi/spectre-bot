# Spectre Bot
A Rasa enabled Discord chatbot based on the work of [DeeJangir](https://github.com/DeeJangir/DiscordBot).

# Features
* Runs Rasa in API mode out of the box
* Automatically trains Rasa when a change occurs in its contents without leaving old model tar files.
* Includes examples of obtaining data through JSON responses, HTML scraping and RSS feeds.
* Exhaustive code comments
* Once the initial setup is performed, running the chatbot requires only one line of code
* OS Independent (I test on Windows and I have the bot running on my Linux server)
* Everything runs in a virutal environment, so you don't have to worry about dependencies

# Current Available Commands
* Weather Information: `-weather cologne` from [OpenWeather](https://openweathermap.org/)
* Corona Stats: `-corona belgium` from [CovidAPI](http://covidapi.com/).
* Fuel Prices: `-fuel` from [Manaseer-Gas](http://mgc-gas.com).
* News: `-news` from [Roya News](https://royanews.tv/)
* Rasa: `!are you a bot?` Requires Rasa to be running. (Refer to _Step 1.2.2_ in this guide)

# Todo
* Valorant API
* Visualizations
* Data store for customized querying per user
* Docker (if needed)
* Better control of switching the bot on and off

# 1 - Setup
This section goes through the setup process, it is split into two sections, one to be done once (per linux install) and the other to be done everytime when the chatbot application is ran.
## 1.1 - One Time Setup
This section goes through the setup process of installing Python and other necessary dependencies to run the chatbot. I will assume
that you have a new Linux install on your server or Raspberry Pi.

### 1.1.1 - Install Python 3.7.7 (New Linux Install)
Note: As of Ubuntu 20.04 LTSC, the default `python3` version is 3.8, therefore, you have to change the 5th
line to `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1`.
``` sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
sudo apt install python3-pip
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1  # Refer to the note above
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
alias python=python3
alias pip=pip3
pip install --upgrade pip
sudo apt install python3.7-venv
```

### 1.1.2 - Install the Virtual Environment Package
``` sh
sudo pip install virtualenv 
```

#### 1.1.2.5 - If Git is not installed, install it
``` sh
sudo apt install git
```

### 1.1.3 - Clone This Repository and Access it
``` sh
git clone https://github.com/ahmadhadidi/spectre-bot.git
cd spectre-bot
```

### 1.1.3 - Create a Virtual Environment
``` sh
python -m venv venv
```
### 1.1.4 - Run The Virtual Environment

``` sh
source venv/bin/activate # Linux
venv\Scripts\activate.bat # Windows
```

### 1.1.5 - Download Dependencies (After Activating the virtual environment)
Please note that you might have to ***run this command twice***, there is an issue with the order of dependencies I guess.

``` sh
pip install -r requirements.txt
```

### 1.1.6 - Discord Token

> Obtain it [here](https://discord.com/developers/applications) by creating an application
> and declaring it as a bot. Refer to [this](https://discordpy.readthedocs.io/en/latest/discord.html) on how to do that.

### 1.1.7 - Create a .env File
``` sh
touch .env
cat .env_example >> .env
```

### 1.1.8 - Fill The Bot Token in .Env
After you've done **1.1.6**, copy the Bot Token and paste it in `.env`
``` sh
sudo nano .env
DiscordBotToken="<INSERT YOUR DISCORD TOKEN HERE>"
```

## 1.2 - Run The Chatbot
### 1.2.1 - Enable The Virtual Environment
``` sh
source venv/bin/activate # Linux
venv\Scripts\activate.bat # Windows
```

### 1.2.2 - Run Both Simultaneously (Recommended)
Deactivate the virtual environment and run the chatbot in a way to prevent it from switching off after closing the terminal window.
``` sh
deactivate # deactivate the virtual environment
nohup venv/bin/python3 main.py & venv/bin/python3 rasa_folder/run_rasa.py
```

### 1.2.3 - Run The Chatbot Without Rasa
After activating the virutal environment. (Refer to Enable The Virtual Environment Section)
``` sh
python main.py
```

### 1.2.4 - Run The Rasa Component for the Chatbot
This python file checks whether if training is needed for Rasa 
and then launches its server. ** Run with venv active **

After activating the virutal environment. (Refer to Enable The Virtual Environment Section)
``` sh
python rasa_folder/run_rasa.py
```

