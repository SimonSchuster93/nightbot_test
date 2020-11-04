import requests
import configZoho as config

auth_code = config.OAUTH_CODE
access_token = config.OAUTH_ACCESS_TOKEN
refresh_token = config.OAUTH_REFRESH_TOKEN
url = config.OAUTH_URL

def get_auth_code_url(client_id=config.CLIENT_ID, redirect_uri=config.REDIRECT_URI, scope='ZohoCRM.settings.ALL'):
    url = f'https://accounts.zoho.com/oauth/v2/auth?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}&prompt=consent&access_type=offline'
    return url

def get_auth_token(auth_code=auth_code, url=url, client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, grant_type='authorization_code', redirect_uri=config.REDIRECT_URI):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'grant_type': grant_type,
        'redirect_uri': redirect_uri
    }
    r = requests.post(url, data=payload)
    return r

def refresh_auth_token(refresh_token, url=url, client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, grant_type='refresh_token', redirect_uri=config.REDIRECT_URI):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': grant_type,
        'redirect_uri': redirect_uri
    }
    r = requests.post(url, data=payload)
    return r

def revoke_token(token):
    payload = {
        'token': token
    }
    r = requests.post(url+'/revoke', data=payload)
    return r

#print(get_auth_code_url())
#print(get_auth_token().text)
#print(refresh_auth_token(refresh_token=refresh_token).text)
#print(revoke_token(token=access_token).text)
