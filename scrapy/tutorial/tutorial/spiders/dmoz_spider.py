import scrapy
from tutorial.items import DmozItem

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
		# filename = response.url.split("/")[-2]
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)

		# for sel in response.xpath('//ul/li'):
		# 	title = sel.xpath('a/text()').extract()
		# 	link = sel.xpath('a/@href').extract()
		# 	desc = sel.xpath('text()').extract()
		# 	print(title, link, desc)

		for sel in response.xpath('//div[@class="title-and-desc"]'):
			item = DmozItem()
			item['title'] = sel.xpath('a/div/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('div/text()').extract()
			# 去掉desc前后多余字符（如多个空格，'\r\n'）
			item['desc'] = item['desc'][0].lstrip()
			item['desc'] = item['desc'].rstrip()
			yield item
	# run cmd: scrapy crawl dmoz			