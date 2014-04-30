#! /usr/bin/env python

from scraper.TasteDotCom import *


class TasteDotComStatic(TasteDotCom):
    """Parse Taste.com.au recipe into components - this is a subclass for testing without Internet
    connectivity, instead an html file is used in place of a URL to parse."""

    def __init__(self, file_name):
        super(TasteDotComStatic, self).__init__('')
        html_text = file(file_name).read()
        self.tree = html.fromstring(html_text)

        self.title = ''
        self.summary = ''
        self.prep_time = ''
        self.ingredients = []
        self.steps = []

        # Now parse the attributes
        self.parse_attributes()