import requests

class Swapi:

	url = 'https://swapi.co/api/'
	name = ''

	def __init__(self, entity):
		self.entity = entity

	def setName(self, name):
		self.name = name	

	def searchQuantityTimesAppeared(self):

		endpoint = self.url+self.entity+'/?format=json&search='+self.name
		timesAppeared = 0

		while True:	
			r = requests.get(endpoint)
			json = r.json()

			for result in json['results']:
				if(result['name'] == self.name):
					timesAppeared = len(result['films'])

			if(json['next']):
				endpoint = json['next']
			else:
				break

		return timesAppeared