from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ['Elie', 'Tim', 'Matt']
    random_name = 'Tom'
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return "Welcome to the second page!"

@app.route('/title')
def title():
	return render_template('title.html')

@app.route('/show-form')
def show_form():
    return render_template('first-form.html')

@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return "You put {} {}".format(first, last)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

