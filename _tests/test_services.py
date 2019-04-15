
import importresolver
import unittest
import random
from random import randrange
import requests
from models.log import Log
from models.dal.mongo import Mongo

class testLogger(unittest.TestCase):

	url = 'http://localhost:5000/'
	parseLog = 'log/parse'
	listLogs = 'log/list'

	log = Log

	def testInsertFileSuccess(self):
		endpoint = self.url+self.parseLog
		
		for x in range(0, 3):
			f = open('/app/fileToSend/log.txt', 'rb')
			fileToSend = {'file': f}
			result = requests.post(endpoint, files=fileToSend)
			self.assertEqual(result.json()['success'], True)
			f.close()

		endpoint = self.url+self.listLogs
		result = requests.get(endpoint)
		# 3 elementos mais a mensagem de sucesso
		self.assertEqual(len(result.json()), 4)

	def testInsertFileFail(self):
		endpoint = self.url+self.parseLog
		
		f = open('/app/fileToSend/python.png', 'rb')
		fileToSend = {'file': f}
		result = requests.post(endpoint, files=fileToSend)
		self.assertEqual(result.json()['success'], False)
		f.close()

		endpoint = self.url+self.listLogs
		result = requests.get(endpoint)
		# 0 elementos mais a mensagem de sucesso
		self.assertEqual(len(result.json()), 1)

	def tearDown(self):
		Dal = Mongo(self.log.collectionName)
		Log = self.log(Dal)
		Log.removeAll()

if __name__ == '__main__':
	unittest.main()