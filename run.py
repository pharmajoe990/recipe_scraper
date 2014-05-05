"""
Run the program.
"""
import pprint
from crawler.Crawler import Crawler
from scraper.TasteDotCom import TasteDotCom

page = "http://www.taste.com.au/"
#todo below is redundant as depth not used
depth = 3

crawler = Crawler(page, depth)
crawler.build_crawl_list()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(crawler.urls)