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

Notes
    -If children is set to 0, Crawler will scan ALL pages.
"""
import re

import requests

from crawler import Page
from scraper import TasteDotCom


def get_urls(html):
    """
    Parse the html passed to this method and find all the URLs or
    Hyperlinks within the markup. This includes all links, such
    as images and other URLs (not restricted).
    """
    return re.findall(r'http://www\.[//\a\w\.\+]+', html)


class Crawler(object):
    def __init__(self, base_page, crawl_depth, children):
        self.urls = []
        self.base_url = base_page
        self.depth = crawl_depth
        self.children = children

    def build_crawl_list(self):
        """
        Build a list of all of the URLs based on the depth specified.
        """
        current_depth = 1
        page = requests.get(self.base_url).text
        if self.children > 0:
            self.urls = Page.get_urls(page)[:self.children]
        else:
            self.urls = Page.get_urls(page)
        # Below list holds previously scanned URLs, to stop URLs being added twice
        scanned_urls = []
        while current_depth <= self.depth:
            # Append the links for each page then search it for more
            print 'Starting crawl depth', current_depth, 'with', len(self.urls), 'URLs to scan'
            new_urls = []
            for url in self.urls:
                # If the url is not already scanned, and if it is not an image, xml etc. scan it.
                if url not in scanned_urls:
                    if TasteDotCom.is_wanted_object(url):
                        print 'Looking for child URLs in ', url
                        markup = requests.get(url).text
                        scanned_urls.append(url)
                        if self.children > 0:
                            new_urls = Page.get_urls(markup)[:self.children]
                        else:
                            new_urls = Page.get_urls(markup)
            print 'Found', len(new_urls), 'new pages'
            # for url in new_urls:
            #     check_and_add(url)
            self.urls += new_urls
            current_depth += 1
        print 'Finished crawling', self.base_url, 'found', len(self.urls), 'total URLs'

    # def run(self):
    #     """
    #     Start Crawling the page specified
    #     """
    #     #todo Make use of this method
    #     print "Starting crawl session for", self.base_url
    #     page = requests.get(self.base_url).text
    #     child_urls = Page.get_urls(page)
    #     for url in child_urls:
    #         self.check_and_add(url)

# def check_and_add(url):
#     pass