class Webscrape1Pipeline(object):
    def process_item(self, item, spider):
        print("Pipeline :" + item['title'][0])
        return item