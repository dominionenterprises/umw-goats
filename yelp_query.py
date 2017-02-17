from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import io

class yelper:
<<<<<<< HEAD

	def __init__(self):

		with io.open('config_secret.json') as cred:
			creds = json.load(cred)
			auth = Oauth1Authenticator(**creds)
			self.client = Client(auth)

	def resturant_search(self, query):
			try:
				params = {
	               'term':'food'
                }
				response = self.client.search(query,**params)
			except Exception as e:
				print(e)
				return None

			data = [0]*5
			for resturant in response.businesses:
				data[int(resturant.rating)-1] +=  1
			"""
				data[business.id] = {"coordinates": (business.location.coordinate.latitude, business.location.coordinate.longitude)}
				print(business.categories)
				print()
			"""
			return data

y =  yelper()

print(y.resturant_search("22407"))




=======
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

        return data

class renter:
    def __init__(self):
        pass

    def search(self, query):
        pass
>>>>>>> master
