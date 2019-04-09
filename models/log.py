from pymongo import MongoClient
import requests
from libraries.swapi import Swapi
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
		f= open(filename,"r")
		text = f.read()
		f.close()
		
		urls = []
		userAgent = []
		ip = []
		date = []
		
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

		#x = 0
		#while x < len(df['url'].value_counts().index.tolist()):
		entity = {}
		for x in range(0, 5):
			entity['url'] = df['url'].value_counts().index[x]
			entity['count'] = df['url'].value_counts().tolist()[x]
			data['url'].append(entity.copy())
			x += 1

		entity = {}
		for x in range(0, 5):
			entity['userAgent'] = df['userAgent'].value_counts().index[x]
			entity['count'] = df['userAgent'].value_counts().tolist()[x]
			data['userAgent'].append(entity.copy())
			x += 1

		entity = {}
		for x in range(0, 5):
			entity['ip'] = df['ip'].value_counts().index[x]
			entity['count'] = df['ip'].value_counts().tolist()[x]
			data['ip'].append(entity.copy())
			x += 1

		return data


	def getAll(self, skip, limit):
		lista = []
		for collection in self.dal.findAll(skip, limit):
			lista.append(collection.copy())
		return lista

	def getById(self, id):
		return self.dal.findById(id)

		
