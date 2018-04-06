from bs4 import BeautifulSoup
import json
import requests


class ArticleSpider():

	articles = []

	def _get_urls(self):
		"""
		Accepts a string of urls (separated by a new line) from standard input.
		
		Returns a list of urls
		"""
		# http://www.bbc.co.uk/sport/tennis/43106776\nhttp://www.bbc.co.uk/sport/tennis/43106898\nhttp://www.bbc.co.uk/sport/tennis/42645676
		urls = input('Enter each url to scrape: ')
		if urls:
			urls = urls.split("\\n")
			return urls

	def _request_url(self, url):
		return requests.get(url)

	def _parse_url(self, url, url_data):
		"""
		Returns a dict populated with article data.
		"""
		data = url_data.text
		soup = BeautifulSoup(data, 'lxml')
		article = {}
		article['url'] = url
		article['headline'] = soup.article.h1.text
		article['images'] = []
		for img in soup.article.find_all('img'):
			article['images'].append({
				'url': img['src'],
				'caption': img.find_next('figcaption').text,
			})
		return article

	def _save_json_to_file(self, filename):
		with open(filename, 'w') as outfile:
			json.dump(self.articles, outfile, indent=2)
		print('Saved to json file.')

	def crawl(self):
		"""
		Driver function.
		"""
		urls = self._get_urls()
		for url in urls:
			url_data = self._request_url(url)
			self.articles.append(self._parse_url(url, url_data))
		self._save_json_to_file('articles.json')


if __name__ == '__main__':
	spider = ArticleSpider()
	spider.crawl()
