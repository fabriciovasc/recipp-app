from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

recipe_ingredient = db.Table('recipe_ingredient',
                             db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
                             db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True),
                             db.Column('amount', db.Integer)
                             )


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    steps = db.Column(db.String(1000), nullable=False)
    ingredients = db.relationship(
        'Ingredient', secondary=recipe_ingredient, lazy='subquery',
        backref=db.backref('recipe', cascade='all,delete', lazy=True)
    )
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'steps': self.steps,
            'created_at': str(self.created_at)
        }


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
