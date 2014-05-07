"""
Taste.com.au crawler. Implements logic specific for the website
www.taste.com.au based on the Parent Crawler class.
"""
from crawler.Crawler import Crawler
from scraper.TasteDotCom import TasteDotCom


class TasteCrawler(Crawler):

        def __init__(self, base_page, crawl_depth, children):
        		Crawler.__init__(self, base_page, crawl_depth, children)
            # super(self).__init__()
            # super.__init__(self, base_page, crawl_depth, children)
          		self.scrapable_urls = []

        def check_and_add(self, url):
            # Check if the URL matches a pattern for a recipe.
            print 'Foobar'
            if self.is_recipe_url(url):
                if url not in self.urls:
                    self.scrapable_urls.append(url)