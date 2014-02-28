#! /usr/bin/env python
#
# Test class runner, decode URL from input

from TasteDotCom import *

if len(sys.argv) != 2:
	print 'Please specify a URL as argument.'
	sys.exit()

testUrl = sys.argv[1]

testUrl = 'http://www.taste.com.au/recipes/34764/steak+sandwich+salad'

parser = TasteDotCom(testUrl)

parser.printDetails()