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
3.  Parse the child pages, one at a time, for any further child pages up to the specified depth.
"""

import requests


class Crawler(object):

    def __init__(self, base_page, crawl_depth, children):
        self.urls = None
        self.base_url = base_page
        self.depth = crawl_depth
        self.children = children

    def run(self):
        """
        Start Crawling the page specified
        """
        print "Starting crawl session for", self.base_url
        page = requests.get(self.base_url).text
        # For each child, find children then check for children until max then go to next parent
        
    def get_urls(page):
        """
        Parse an html page and retrieve the URLs (hyperlinks) that exist in it  
        """
        pass