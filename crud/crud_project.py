import requests
import json
import webbrowser

data = requests.get('https://spreadsheets.google.com/feeds/list/1sYkU_8raV14Bqm33dWcaksC3iMm73DH9OMsooxSMItM/od6/public/values?alt=json')

data = data.json()

print(data)

