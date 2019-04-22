
import importresolver
import unittest
import random
from random import randrange
import requests
from models.log import Log
from models.dal.mongo import Mongo

class testLoggerModel(unittest.TestCase):

	log = Log

	def testInsertLogFail(self):
		Dal = Mongo(self.log.collectionName)
		Log = self.log(Dal)
		with self.assertRaises(OSError):
			Log.process('/app/fileToSend/arquivoinexistente.txt')

	def testInsertLogSuccess(self):
		Dal = Mongo(self.log.collectionName)
		Log = self.log(Dal)
		self.assertEqual(len(str(Log.process('/app/fileToSend/log.txt'))), 24)

	def setUp(self):
		Dal = Mongo(self.log.collectionName)
		Log = self.log(Dal)
		Log.removeAll()

	def tearDown(self):
		Dal = Mongo(self.log.collectionName)
		Log = self.log(Dal)
		Log.removeAll()

if __name__ == '__main__':
	unittest.main()