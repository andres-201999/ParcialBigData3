from flask  import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
data={}

@app.route('/', methods=['POST'])
def receive_data():
  hashtag = request.form['hashtag']
  count = request.form['count']
  data[hashtag] = count
  print('Recibido',hashtag,count)
  return 'Dato recibido'

@app.route('/dashboard')
def dashboard():
  return data


app.run('0.0.0.0')

