from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import io

class yelper:

    def __init__(self):

        with io.open('config_secret.json') as cred:
            creds = json.load(cred)
            auth = Oauth1Authenticator(**creds)
            self.client = Client(auth)

    def search(self, query):
            try:
                response = self.client.search(query)
            except Exception as e:
                print(e)
                return None

            data = {}
            for business in response.businesses:

                data[business.id] = {"coordinates": (business.location.coordinate.latitude, business.location.coordinate.longitude)}
                for i in dir(business):
                    print(i, getattr(business, i))
                break
            return data

y =  yelper()
print(y.search("Norfolk"))
