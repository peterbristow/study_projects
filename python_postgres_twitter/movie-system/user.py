import json

from movie import Movie


class User:
	def __init__(self, name):
		self.name = name
		self.movies = []

	def __repr__(self):
		return "<User {}>".format(self.name)

	def add_movie(self, name, genre):
		self.movies.append(Movie(name, genre, False))

	def delete_movie(self, name):
		self.movies = filter(lambda movie: movie.name != name, self.movies)

	def watched_movies(self):
		return filter(lambda movie: movie.watched, self.movies)

	def set_watched(self, movie_name):
		for movie in self movies:
			if movie.name == movie_name:
				movie.watched = True

	def save_to_csv(self):
		with open("{}.csv".format(self.name), 'w') as f:
			f.write(self.name + "\n")
			for movie in self.movies:
				f.write("{},{},{}\n".format(movie.name, movie.genre, movie.watched))

	@classmethod
	def load_from_csv(cls, filename):
		with open(filename, 'r') as f:
			content = f.readlines()
			username = content[0]
			movies = []
			for line in content[1:]:
				movie_data = line.split(',')  # ['name', 'genre', 'watched']
				movies.append(Movie.from_csv(movie_data))

			user = cls(username)
			user.movies = movies
			return user

	def to_json(self):
		return {
			'name': self.name,
			'movies': [
				movie.json() for movie in self.movies
			]
		}

	@classmethod
	def from_json(cls, json_data):
		user = User(json_data['name'])
		movies = []
		for movie_data in json_data['movies']:
			movies.append(Movie.from_json(movie_data))
		user.movies = movies

		return user
