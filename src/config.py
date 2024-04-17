from routes.filmes import filme_route

from database.database import db
from database.Models.filmes import Filmes


def configure_all(app):
    configure_db()
    configure_routes(app)

def configure_db():
    db.connect()
    db.create_tables([Filmes])

def configure_routes(app):
    app.register_blueprint(filme_route,url_prefix='/filmes')