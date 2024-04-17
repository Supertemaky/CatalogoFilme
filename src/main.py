from flask import Flask, render_template, url_for
from routes.filmes import filme_route
from config import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('listar_filmes.html')

configure_all(app)

app.run(debug=True)