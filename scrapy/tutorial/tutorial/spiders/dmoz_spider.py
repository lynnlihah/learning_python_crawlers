import scrapy

class DomzSpider(scrapy.spiders.Spider):
	"""docstring for DomzSpider"""
	# def __init__(self, arg):
	# 	super(DomzSpider, self).__init__()
	# 	self.arg = arg
	name = "dmoz"
	allowed_domains = ["dmoztools.net"]
	start_urls = [ # old: http://www.dmoz.org/ - image: dmoztools.net
		"http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
		"http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
	
	# run cmd: scrapy crawl dmoz			