from flask import Flask
from config import *

app = Flask(__name__)

@app.route('/')
def main():
    return 'teste'

configure_all(app)

app.run(debug=True)