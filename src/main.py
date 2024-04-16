from flask import Flask, render_template, url_for
from routes.filmes import filme_route
from config import *

app = Flask(__name__)

app.register_blueprint(filme_route, url_prefix="/filmes")

@app.route('/')
def main():
    return 'teste'

configure_all(app)

app.run(debug=True)