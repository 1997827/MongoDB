from .db import db

class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    birth = db.ListField(db.StringField(), required=True)
    death = db.ListField(db.StringField(), required=True)
    contribs = db.ListField(db.StringField(), required=True)
    views = db.ListField(db.StringField(), required=True)
        