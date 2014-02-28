#! /usr/bin/env python

# Parse an html recipe file into it's specific content

from lxml import html
import requests

fileName = '/home/timbo/Documents/sample_recipes/minute_steak_with_romesco_salad.html'
inputFile = open(fileName, 'r')
tree = html.fromstring(inputFile.read())

# Parse the properties etc.
title = tree.xpath('//h1[@itemprop="name"]/text()')
summary = tree.xpath('//p[@itemprop="summary"]/text()')
prep_time = tree.xpath('//em[@itemprop="prepTime"]/text()')

# Parse the Ingredients
ingredients = tree.xpath('//ul[@class="ingredient-table"]//span[@class="element"]/text()')

# Parse the steps
steps = tree.xpath('//div[@class="content-item tab-content current method-tab-content"]/ol//li[@class="methods"]/p[@class="description"]//text()')

print title[0]
print summary[0]
print prep_time[0]

print "\n", "Ingredients:", "\n"

for i in ingredients:
	print i	

print "\n", "Method:", "\n"
count = 0
for s in steps:
	print count, '.', '\t', s.lstrip().rstrip()
	count += 1
