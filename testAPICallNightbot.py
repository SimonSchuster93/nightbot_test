import oAuthNightbot as oAuth
import requests

r = requests.get('https://api.nightbot.tv/1/me', headers={'Authorization': 'Bearer ' + oAuth.access_token})
print(r.text)
