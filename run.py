"""
Run the program.
"""

from crawler.TasteCrawler import TasteCrawler
from scraper.TasteDotCom import TasteDotCom


page = "http://www.taste.com.au/"
depth = 3
children = 0

crawler = TasteCrawler(page, depth, children)
crawler.build_crawl_list()
recipes = []
for url in crawler.scrapable_urls:
    t = TasteDotCom(url)
    recipes.append()
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(crawler.urls)