#! /usr/bin/env python
#
# Test class runner for static file

from TasteDotComStatic import *

if len(sys.argv) != 2:
	print 'Please specify a URL as argument.'
	sys.exit()

testUrl = sys.argv[1]

fileName = sys.argv[1]

parser = TasteDotComStatic(fileName)

# parser.printDetails()

print parser.getJSON()