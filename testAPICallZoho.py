import oAuthZoho as oAuth
import requests

r = requests.get('https://www.zohoapis.eu/crm/v2/settings/modules', headers={'Authorization': 'Zoho-oauthtoken ' + oAuth.access_token})
print(r.text)
