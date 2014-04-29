#! /usr/bin/env python

# Parse an html recipe file that is hard-coded for testing into it's specific content

from TasteDotCom import *

from lxml import html


class TasteDotComStatic(TasteDotCom):
    """Parse Taste.com.au recipe into components - this is an overloaded method for testing without internet
    connectivity"""

    def __init__(self, file_name):
        # Load the text from file
        html_file = file(file_name)
        html_text = html_file.read()
        self.tree = html.fromstring(html_text)

        # Parse the properties etc.
        self.title = self.tree.xpath('//h1[@itemprop="name"]/text()')[0]
        self.summary = self.tree.xpath('//p[@itemprop="summary"]/text()')[0]
        self.prep_time = self.tree.xpath('//em[@itemprop="prepTime"]/text()')[0]

        # Parse the Ingredients
        self.ingredients = self.tree.xpath('//ul[@class="ingredient-table"]//span[@class="element"]/text()')

        # Parse the steps
        self.steps = self.tree.xpath(
            '//div[@class="content-item tab-content current method-tab-content"]/ol//li[@class="methods"]/'
            'p[@class="description"]//text()')