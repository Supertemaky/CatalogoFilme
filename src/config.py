from routes.filmes import filme_route

from database.database import db
from database.Models import Filme 


def configure_all():
    pass

def configure_db():
    db.connect()
    db.create_tables([Filme])