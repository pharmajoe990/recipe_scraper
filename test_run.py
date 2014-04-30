#! /usr/bin/env python
#
# Test class runner, decode URL from input
# todo Convert this to Test-Driven class

import sys

from scraper.TasteDotCom import *

if len(sys.argv) != 2:
    print 'Please specify a URL as argument.'
    sys.exit()

testUrl = sys.argv[1]

# testUrl = 'http://www.taste.com.au/recipes/34764/steak+sandwich+salad'

parser = TasteDotCom(testUrl)

parser.print_details()