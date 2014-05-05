from crawler.Crawler import Crawler

__author__ = 'tim'

import unittest


class CrawlerTest(unittest.TestCase):
    def test_get_children(self):
        page = "http://www.taste.com.au/"
        # Exclude depth for now
        depth = 3
        # children = 3
        crawler = Crawler(page, depth)
        crawler.run()
        # Should have depth*children urls from crawl result
        self.assertGreater(len(crawler.urls), 1)
        print crawler.urls