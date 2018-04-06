"""Users and messages app."""
from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/users-messages"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)
db = SQLAlchemy(app)
# Migrate(app, db)


class User(db.Model):
    """Users."""

    __tablename__ = "users"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship('Message', backref="user", lazy="dynamic", cascade="all, delete")
    # Above relationship allows (one to many):
    # If we find a specific user we can do:  user.messages
    # Also if we find a specific message, we can do:  message.user
    # cascade - If user deleted, will also delete all related messages as well.

    def __init__(self, first_name, last_name):
        """init."""
        self.first_name = first_name
        self.last_name = last_name


class Message(db.Model):
    """Messages."""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, content, user_id):
        """init."""
        self.content = content
        self.user_id = user_id


@app.route('/')
def root():
    """Root."""
    return redirect(url_for('index'))


@app.route('/users', methods=["GET", "POST"])
def index():
    """Index."""
    if request.method == "POST":
        new_user = User(request.form['first_name'], request.form['last_name'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/index.html', users=User.query.all())


@app.route('/users/new')
def new():
    """New."""
    return render_template('users/new.html')


@app.route('/users/<int:id>/edit')
def edit(id):
    """Edit user."""
    return render_template('users/edit.html', user=User.query.get(id))


@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    """Show user."""
    found_user = User.query.get(id)
    if request.method == b"PATCH":
        found_user.first_name = request.form['first_name']
        found_user.last_name = request.form['last_name']
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == b"DELETE":
        db.session.delete(found_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/show.html', user=found_user)


# See all messages for a specific user
# and create a message for a specific user
@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def messages_index(user_id):
    """Message index. Find a user."""
    if request.method == "POST":
        new_message = Message(request.form['content'], user_id)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('messages_index', user_id=user_id))
    return render_template('messages/index.html', user=User.query.get(user_id))


@app.route('/users/<int:user_id>/messages/new', methods=['GET', 'POST'])
def messages_new(user_id):
    """Message new."""
    return render_template('messages/new.html', user=User.query.get(user_id))


@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
    """Message edit."""
    found_message = Message.query.get(id)
    return render_template('messages/edit.html', message=found_message)


@app.route('/users/<int:user_id>/messages/<int:id>/edit', methods=['GET', 'PATCH', 'DELETE'])
def messages_show(user_id, id):
    """Message show."""
    found_message = Message.query.get(id)
    if request.method == b"PATCH":
        found_message.content = request.form['content']
        db.session.add(found_message)
        db.session.commit()
        return redirect(url_for('messages_index', user_id=user_id))
    if request.method == b"DELETE":
        db.session.delete(found_message)
        db.session.commit()
        return redirect(url_for('messages_index', user_id=user_id))
    return render_template('messages/show.html', message=found_message)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
