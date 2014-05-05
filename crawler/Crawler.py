"""
Web Crawler - crawl a website looking for pages to scrape data from. Pages
will be crawled up to a level of depth. Eg. if depth of 3 is specified, pages will be crawled
3 levels below the page at the base URL ie.

base_url
    -child level 1
        -child level 2
            -child level 3

The Crawler operates thus
1.  Send request for the base URL which will be the parent page of all children.
2.  Parse the document at the base URL for any child pages in the base URL.
3.  Parse the child pages, one at a time, for any further child pages up to the
    specified depth.
"""
import re

import requests
from crawler import Page


class Crawler(object):
    def __init__(self, base_page, crawl_depth):
        self.urls = []
        self.base_url = base_page
        self.depth = crawl_depth

    def run(self):
        """
        Start Crawling the page specified
        """
        print "Starting crawl session for", self.base_url
        page = requests.get(self.base_url).text
        child_urls = Page.get_urls(page)
        for url in child_urls:
            # Check if the URL matches a pattern for a recipe.
            if re.match(r'http://www.taste.com.au/recipes/\d+/[\w+]+', url):
                self.urls.append(url)

