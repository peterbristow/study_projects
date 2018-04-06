import scrapy


class ArticlesSpider(scrapy.Spider):
	name = "articles"

	data = []

	def url_requests(self):
		urls = self.get_urls
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		"""
		Builds the data object.

		Returns a dict
		"""
		input_url = response.url
		self.data.append({
			'url': input_url,
		})

	def driver():
		url_requests()
		return self.data

	def get_urls():
	"""
	Accepts a list of urls (separated by a new line) from standard input.
	
	Returns a list of urls
	"""
	# urls = input('Enter each url to scrape: ')
	urls = 'http://www.bbc.co.uk/sport/tennis/37268846'  #PJB: Remove after testing, uncomment above line.
	if urls:
		urls = urls.split("\\n")
		return urls

print(ArticlesSpider.driver())