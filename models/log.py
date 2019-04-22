from pymongo import MongoClient
import requests
#from libraries.swapi import Swapi
from models.dal.basedal import BaseDal
from models.exceptions.planet import PlanetException
import re
import pandas as pd
import json

class Log:

	collectionName = 'log'

	def __init__(self, dal : BaseDal):
		self.dal = dal

	def setId(self, id):
		self.id = str(id)

	def process(self, filename):
		try:
			f= open(filename,"r")
			text = f.read()
			f.close()
		except:
			raise OSError()
			
		
		urls = []
		userAgent = []
		ip = []
		date = []
		
		#Sem quebras de linha
		for logLine in text.split('- - - - -'):
			if logLine.strip():
				#Buscando o que está entre aspas e entre colchetes
				entitiesInQuotes = re.findall(r'"(.*?)"', str(logLine))
				entitiesInBrackets = re.findall(r"\[.*?\]", str(logLine))
				
				#Preparando para montar o data frame
				urls.append(entitiesInQuotes[1])
				userAgent.append(entitiesInQuotes[2])
				ip.append(entitiesInQuotes[3])
				date.append(entitiesInBrackets[0])

		df = pd.DataFrame({'url' : urls, 'userAgent' : userAgent, 'ip' : ip, 'date' : date})
		data = self.__parseToDatabase(df)	
		return self.dal.insert(data)


	def __parseToDatabase(self, df):
		data = {'url' : [], 'userAgent' : [], 'ip' : []}
		
		columns = df.columns.tolist()
		for column in columns:
			entity = {}
			x = 0
			if data.get(column) != None:
				for x in range(0, 5):
					entity['count'] = df[column].value_counts().tolist()[x]
					entity[column] = df[column].value_counts().index[x]
					data[column].append(entity.copy())
					x += 1

		return data


	def getAll(self, skip, limit):
		lista = []
		for collection in self.dal.findAll(skip, limit):
			lista.append(collection.copy())
		return lista

	def getById(self, id):
		return self.dal.findById(id)

	def removeAll(self):
		return self.dal.removeAll()

		
