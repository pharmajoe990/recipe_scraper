from crawler import Page

__author__ = 'tim'

import re
import unittest


class PageTest(unittest.TestCase):
    def test_get_urls(self):
        # Use a known static page for testing
        html = file("../miscellany/sausage_and_punpkin_curry.html").read()
        urls = Page.get_urls(html)
        self.assertEquals(len(urls), 387)
        a = re.compile("'http://www\.[//\a\w\.\+]+'")
        # for url in urls:
        #     # Check each URL matches a hyperlink pattern
        #     self.assertTrue(a.match(url))