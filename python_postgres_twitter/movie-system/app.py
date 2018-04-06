import json
import os

from movie import Movie
from user import User


def menu():
	name = raw_input("Enter your name: ")
	filename = "{}.json".format(name)
	if file_exists(filename):
		with open(filename, 'r') as f:
			json_data = json.load(f)
		user = User.from_json(json_data)
	else:
		user = User(name)

	user_input = raw_input("Enter 'a' to add a movies, 's' to see a list of movies, 'w' to set a movies as watched, "
		"'d' to delete a movie, 'l' to se a list of watched movies or 'q' to save and quit: ")
	if user_input == 'a':
		movie_name = raw_input("Enter the movie name: ")
		genre = raw_input("Enter the movie genre: ")
		user.add_movie(movie_name, genre)
	elif user_input == 's':
		for movies in user.movies:
			print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))
	elif user_input == 'w':
		movie_name = raw_input("Enter the movie name to set as watched: ")
		user.set_watched(movie_name)
	elif user_input == 'd':
		pass
	elif user_input == 'l':
		pass
	elif user_input == 'q':
		pass


def file_exists(filename):
	return os.path.isfile(filename)

menu()