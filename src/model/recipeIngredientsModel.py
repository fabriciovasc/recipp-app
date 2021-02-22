from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RecipeIngredients(db.model):
    id = db.Column(db.Integer, primary_key=True)
    id_ingredient = db.Column(db.Integer, nullable=False)
    id_recipe = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
