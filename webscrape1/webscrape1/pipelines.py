import sqlite3


class Webscrape1Pipeline(object):

	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect("my_quotes.db")
		self.curr = self.conn.cursor()

	def create_table(self):
		self.curr.execute("""create table if not exists quotes_tb(
			title text,
			author text,
			tags text)""" )

	def process_item(self, item, spider):
		self.store_db( item)
		return item

	def store_db(self, item):
		self.curr.execute("""insert into quotes_tb(title, author, tags) values(?,?,?)""",(
			item['title'][0],
			item['author'][0],
			item['tags'][0]) )
		self.conn.commit()