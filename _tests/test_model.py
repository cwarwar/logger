
import importresolver
import unittest
import random
from random import randrange
from models.planet import Planet
from models.dal.mongo import Mongo

class testPlanetModel(unittest.TestCase):
	def testInsertPlanet(self):
		
		randNumber = str(randrange(0, 10000))
		name = 'name_test'+randNumber
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()

		#Buscando o planeta
		self.Planet.setId(str(storedPlanetId))
		planetData = self.Planet.getById()

		#Comparando o planeta inserido com o buscado
		self.assertEqual(storedPlanetId, planetData['_id'])
		self.assertEqual(name, planetData['name'])
		self.assertEqual(weather, planetData['weather'])
		self.assertEqual(terrain, planetData['terrain'])
		

	def testTimesPlanetAppeared(self):

		randNumber = str(randrange(0, 10000))
		name = 'Naboo'
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()

		#Buscando o planeta
		self.Planet.setId(str(storedPlanetId))
		planetData = self.Planet.getById()
		#Removendo o planeta
		self.Planet.remove()

		self.assertEqual(4, planetData['timesAppeared'])

	def testListPlanets(self):

		'''
		Inserindo 10 planetas para garantir
		uma massa de testes
		'''
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)

		for x in range (0, 10):
			randNumber = str(randrange(0, 10000))
			name = 'name_test'+randNumber
			weather = 'weather_test'+randNumber
			terrain = 'terrain_test'+randNumber

			self.Planet.setName(name)
			self.Planet.setWeather(weather)
			self.Planet.setTerrain(terrain)
			storedPlanetId = self.Planet.store()

		#Testando 10 limits diferentes
		for y in range (0, 10):
			limit = random.randrange(1, 10)
			planets = self.Planet.getAll(0, limit)
			self.assertEqual(limit, len(planets))

	def testGetPlanetByName(self):
		randNumber = str(randrange(0, 10000))
		name = 'name_test'+randNumber
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()
		planetRetrieved = self.Planet.getByName()

		self.assertEqual(storedPlanetId, planetRetrieved[0]['_id'])

	def testRemovePlanet(self):
		randNumber = str(randrange(0, 10000))
		name = 'name_test'+randNumber
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()

		self.Planet.setId(str(storedPlanetId))
		quantityPlanetsRemoved = self.Planet.remove()
		self.assertEqual(1, quantityPlanetsRemoved)



	#Faltando testar as falhas :(


if __name__ == '__main__':
    unittest.main()