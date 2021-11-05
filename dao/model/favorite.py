from marshmallow import Schema, fields

from setup_db import db


class Favorite(db.Model):
    __tablename__ = 'faivorite_movie'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))


class Favorite_movieSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()