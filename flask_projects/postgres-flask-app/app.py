"""Toys app."""
from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
import db


app = Flask(__name__)
modus = Modus(app)


@app.route('/toys', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db.add_toy(request.form['name'])
        return redirect(url_for('index'))
    return render_template('index.html', toys=db.get_all_toys())


@app.route('/toys/new')
def new():
    return render_template('new.html')


@app.route('/toys/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_toy = db.get_toy(id)
    if request.method == b'PATCH':
        name = request.form['name']
        db.edit_toy(id, name)
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        db.delete_toy(id)
        return redirect(url_for('index'))
    return render_template('show.html', toy=found_toy)


@app.route('/toys/<int:id>/edit')
def edit(id):
    found_toy = db.get_toy(id)
    return render_template('edit.html', toy=found_toy)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
