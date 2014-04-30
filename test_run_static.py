#! /usr/bin/env python
#
# Test class runner for static file
# todo Convert this to Test-Driven class

import sys

from scraper.TasteDotComStatic import *

if len(sys.argv) != 2:
    print 'Please specify an HTML file as argument.'
    sys.exit()

fileName = sys.argv[1]

parser = TasteDotComStatic(fileName)

# parser.printDetails()

print parser.get_json()