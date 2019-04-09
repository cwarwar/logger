#import pymysql

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)

@app.route('/planets/list')
def listPlanets():
	print(vars(request))
	return 'listagem de planetas'

@app.route('/planets/getByName/<name>')
def getPlanetsByName(name):
	return name

@app.route('/planets/getById/<id>')
def getPlanetsById(id):
	return id

@app.route('/planets/remove/<id>')
def removePlanet(id):
	return username


if __name__ == '__main__':
     app.run(port='5002')