from yelp.client import Client
from yelp.oauth1_authenticator import OauthAuthenticator

with io.open('config_secret.json') as cred:
	creds = json.load(cred)
	auth = Oauth1Authenticator(**creds)
	client = Client(auth)

params = {
	;
}

client.search('San Francisco', **params)

