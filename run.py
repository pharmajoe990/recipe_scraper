"""
Run the program.
"""
from crawler.Crawler import Crawler
from scraper.TasteDotCom import TasteDotCom

page = "http://www.taste.com.au/"
#todo below is redundant as depth not used
depth = 3

crawler = Crawler(page, depth)
crawler.run()
for recipe_url in crawler.urls:
    t = TasteDotCom(recipe_url)
    print 'Scraping details for', t.title
    # t.print_details()
