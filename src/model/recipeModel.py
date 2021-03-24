from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    steps = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
