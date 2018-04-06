"""Alchemy - Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/computers-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Computer(db.Model):
    """Notice that all models inherit from SQLAlchemy's db.Model."""

    __tablename__ = "computers"  # table name will default to name of the model

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    memory_in_gb = db.Column(db.Integer)

    def __init__(self, name, memory_in_gb):
        """Define what each instance or row in the DB will have.
        (id is taken care of for you).
        """
        self.name = name
        self.memory_in_gb = memory_in_gb

    def __repr__(self):
        """Not essential, but a valuable method to overwrite.
        This is what we will see when we print out an instance in a REPL.
        """
        return "This {} has {} GB of memory".format(
            self.name,
            self.memory_in_gb
        )
