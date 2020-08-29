import requests

r = requests.get('https://dds-weather-server.herokuapp.com/weather?address=chicago')

print(r.json())
