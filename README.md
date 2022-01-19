# Rasa_Compound_Bot_Flask with GUI
# Flight Search Rasa_Chatbot

## create virtual environment
```
python3 -m venv venv
```
## activate virtual environment
```
source venv/bin/activate
```
## Install rasa2.0
```
pip install rasa==2.8.9
```
## create initial bot
```
rasa init --no-prompt
```
## Replace all file 
## For trainig
```
rasa train
```
## For test
```
rasa run actions
```
##open another terminal tab
```
rasa run -m models --enable-api --cors “*” --debug -p 5000
```
##open html file in any browser
