class Movie:
	def __init__(self, name, genre, watched):
		self.name = name
		self.genre = genre
		self.watched = watched

	def __repr__(self):
		return "<Movie {}>".format(self.name)

	@classmethod
	def from_csv(cls, csv_data):
		"""
		csv_data = ['name', 'genre', 'watched']
		"""
		return Movie(csv_data[0], csv_data[1], csv_data[2] == 'True')

	def json(self):
		return {
			'name': self.name,
			'genre': self.genre,
			'watched': self.watched
		}

	@classmethod
	def from_json(cls, json_data):
		return Movie(**json_data)