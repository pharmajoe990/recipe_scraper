"""
Run the program.
"""
import pprint

from crawler.Crawler import Crawler


page = "http://www.taste.com.au/"
#todo below is redundant as depth not used
depth = 5
children = 30

crawler = Crawler(page, depth, children)
crawler.build_crawl_list()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(crawler.urls)