"""
A Crawler page, which can be parsed for references to child pages.
"""
import re


def get_urls(html):
    """
    Parse the html passed to this method and find all the URLs or
    Hyperlinks within the markup. This includes all links, such
    as images and other URLs (not restricted).
    """
    return re.findall(r'http://www\.[//\a\w\.\+]+', html)