import scrapy
from ..items import Webscrape1Item


class QuotesSpider( scrapy.Spider ):
	name = "crawler"
	start_urls = [
		'http://quotes.toscrape.com/'
		]


	def parse( self, response ):

		all_quotes = response.css("div.quote")

		item = Webscrape1Item()

		for quote in all_quotes:

			text = quote.css('span.text::text').extract()
			author = quote.css('.author::text').extract()
			tags = quote.css('a.tag::text').extract()
			
			item['title'] = text
			item['author'] = author
			item['tags'] = tags

			yield item

		next_page = response.css("li.next a::attr(href)").get()

		if( next_page != None ):
			yield response.follow(next_page, callback = self.parse )

