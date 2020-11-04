import requests
import configTwitch as config

auth_code = config.OAUTH_CODE
access_token = config.OAUTH_ACCESS_TOKEN
refresh_token = config.OAUTH_REFRESH_TOKEN
url = config.OAUTH_URL

def get_auth_code_url(client_id=config.CLIENT_ID, redirect_uri=config.REDIRECT_URI, scope=['analytics:read:extensions', 'bits:read']):
    scopes = ''
    first = True
    for item in scope:
        if first:
            scopes += item
            first = False
        else:
            scopes += '%20'
            scopes += item

    url = f'https://id.twitch.tv/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scopes}'
    return url

def get_auth_token(auth_code, url=url, client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, grant_type='authorization_code', redirect_uri=config.REDIRECT_URI):
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
    }
    r = requests.post(url, data=payload)
    return r

def revoke_token(token, client_id=config.CLIENT_ID):
    payload = {
        'token': token,
        'client_id': client_id
    }
    r = requests.post('https://id.twitch.tv/oauth2/revoke', data=payload)
    return r

#print(get_auth_code_url())
#print(get_auth_token(auth_code=auth_code).text)
#print(refresh_auth_token(refresh_token=refresh_token).text)
#print(revoke_token(token=access_token).text)
