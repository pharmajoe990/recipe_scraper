import re
from lxml import html
import requests


class TasteDotCom(object):
    """Parse Taste.com.au recipe into components"""

    def __init__(self, url):
        if url != '':
            self.url = url
            self.page = requests.get(self.url)
            self.tree = html.fromstring(self.page.text)

            self.title = ''
            self.summary = ''
            self.prep_time = ''
            self.ingredients = []
            self.steps = []

            # Now parse the attributes (if it is a valid recipe page)
            if is_recipe_url(url):
                self.parse_attributes()
            else:
                print 'Skipping', url, ' as it doesn\'t fit the pattern for a recipe'

    def parse_attributes(self):
        """Parse the html document into Recipe components"""
        # Parse the properties etc.
        #todo Handle errors, eg. cannot parse title, summary etc.
        self.title = self.tree.xpath('//h1[@itemprop="name"]/text()')[0]
        self.summary = self.tree.xpath('//p[@itemprop="summary"]/text()')[0]
        self.prep_time = self.tree.xpath('//em[@itemprop="prepTime"]/text()')[0]

        # Parse the Ingredients
        self.ingredients = self.tree.xpath('//ul[@class="ingredient-table"]//span[@class="element"]/text()')

        # Parse the steps
        self.steps = self.tree.xpath(
            '//div[@class="content-item tab-content current method-tab-content"]/ol//li[@class="methods"]/'
            'p[@class="description"]//text()')

    def print_details(self):
        """Print the details of the parsed recepe to the console"""
        print self.title
        print self.summary
        print self.prep_time

        print "\n", "Ingredients:", "\n"

        for i in self.ingredients:
            print i

        print "\n", "Method:", "\n"
        count = 0
        for s in self.steps:
            print count, '.', '\t', s.lstrip().rstrip()
            count += 1

    def get_json(self):
        """Get JSON Object for this Recipe"""
        json_text = '{\"title\":\"' + self.title + '\",'
        json_text += '\"summary\":\"' + self.summary + '\",'
        json_text += '\"preparation time\":\"' + self.prep_time + '\",'
        # Ingredients
        json_text += '\"ingredients\":['
        for i in self.ingredients:
            json_text += '\"' + i + '\",'
        json_text = json_text[:-1]
        json_text += ']'
        json_text += ','
        # Now add the steps to create
        json_text += '\"steps\":['
        for s in self.steps:
            json_text += '\"' + s + '\",'
        json_text = json_text[:-1]
        json_text += ']'
        json_text += '}'
        # json_text += ''
        # json_text += ''
        return json_text


def is_recipe_url(url):
    """
    Check if the url is valid, ie. matches the required format of a URL that can be scraped for data.
    """
    if re.match(r'http://www.taste.com.au/recipes/\d+/[\w+]+', url):
        return True
    else:
        return False


def is_wanted_object(url):
    """
    Check if the object is something we want; we don't want images, xml etc. This is for use in the Crawler logic,
    where we don't want to crawl objects that won't have markup to crawl for links or scrape data from.
    """
    if re.match(r'http://www.taste.com.au/[\w/]+.(jpg|png|ico|xml)$', url):
        return False
    else:
        return True