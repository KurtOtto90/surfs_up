# Import flask
from flask import Flask

#create Flask app Instance
app = Flask(__name__)

#Create route
@app.route('/')
def hello_world():
    return 'Hello World'
    
