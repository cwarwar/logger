
import os
from flask import Flask, request, jsonify, flash, redirect, url_for, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from models.log import Log
from models.dal.mongo import Mongo
import json

#Ajustar
ALLOWED_EXTENSIONS = set(['txt'])
UPLOAD_FOLDER = '/app/filesReceived'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

Dal = Mongo(Log.collectionName)
Log = Log(Dal)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/log/parse', methods=['POST'])
def parse():
	f = request.files['file']
	if allowed_extensions(f.filename):
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return formatResponse(Log.process(f.filename))

@app.route('/log/list', defaults={'skip' : 0,'limit' : 10})
@app.route('/log/list/<skip>/<limit>', methods=['GET'])
def getAll(skip, limit):
	return formatResponse(Log.getAll(skip, limit))

def allowed_extensions(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def formatResponse(data, success = True):
	response = {
		'success' : success,
		'response' : str(data)
	}
	return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')