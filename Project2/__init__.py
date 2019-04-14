import os
from flask import Flask



app = Flask(__name__)

# to set the environment variables
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from Project2 import routes
