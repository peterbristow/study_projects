import scrapy


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


print(get_urls())

# class ArticlesSpider(scrapy.Spider):
# 	name = "articles"

# 	def start_requests