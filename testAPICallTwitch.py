import oAuthTwitch as oAuth
import requests

r = requests.get('https://api.twitch.tv/helix/search/channels?query=a_seagull', headers={'client-id': oAuth.config.CLIENT_ID,'Authorization': 'Bearer ' + oAuth.access_token})
print(r.text)
