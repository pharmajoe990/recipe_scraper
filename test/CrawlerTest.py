from crawler.Crawler import Crawler

__author__ = 'tim'

import unittest


class CrawlerTest(unittest.TestCase):
    def test_get_children(self):
        page = "http://www.taste.com.au/"
        depth = 3
        children = 2
        crawler = Crawler(page, depth, children)
        crawler.run()
        # Should have depth*children urls from crawl result
        self.assertEqual(len(crawler.urls), depth*children)