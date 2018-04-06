"""Student db using alchemy and flask migrates."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgres://localhost/learn-flask-migrate')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
Migrate(app, db)

# export FLASK_APP=app.py
# flask db migrate
# flask db upgrade


class Student(db.Model):
    """
    Student class.

    backref is used for foreign keys and lazy is used for joins etc.
    """

    __tablename__ = "students"

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    excuses = db.relationship('Excuse', backref='students', lazy='joined')

    # define what each instance or row in the DB will have.
    def __init__(self, first_name, last_name):
        """init."""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        """Repr."""
        return "The student's name is {} {}".format(self.first_name, self.last_name)


class Excuse(db.Model):
    """Excuse table."""

    __tablename__ = "excuses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    is_believable = db.Column(db.Boolean)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __init__(self, name, is_believable, student_id):
        """init."""
        self.name = name
        self.is_believable = is_believable
        self.student_id = student_id

    def __repr__(self):
        """Repr."""
        return "The excuse name is {} {} {}".format(self.name, self.is_believable, self.student_id)


@app.route('/')
def hello_world():
    """Index route."""
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
