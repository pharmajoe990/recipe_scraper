#! /usr/bin/env python

# Parse an html recipe file into it's specific content

from lxml import html
import requests
import sys

page = ''
title = ''
summary = ''
prep_time = ''
ingredients = []
steps = []

class TasteDotCom(object):
	"""Parse Taste.com.au recipe into components"""

	def __init__(self, url):
		self.url = url
		self.page = requests.get(self.url)
		self.tree = html.fromstring(self.page.text)

		# Parse the properties etc.
		self.title = self.tree.xpath('//h1[@itemprop="name"]/text()')[0]
		self.summary = self.tree.xpath('//p[@itemprop="summary"]/text()')[0]
		self.prep_time = self.tree.xpath('//em[@itemprop="prepTime"]/text()')[0]

		# Parse the Ingredients
		self.ingredients = self.tree.xpath('//ul[@class="ingredient-table"]//span[@class="element"]/text()')

		# Parse the steps
		self.steps = self.tree.xpath('//div[@class="content-item tab-content current method-tab-content"]/ol//li[@class="methods"]/p[@class="description"]//text()')

	def printDetails(self):
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

	def getJSON(self):
		"""Get JSON Object for this Recipe"""
		jsonText =  '{\"title\":\"' + self.title + '\",'
		jsonText += '\"summary\":\"' + self.summary + '\",'
		jsonText += '\"preparation time\":\"' + self.prep_time + '\",'		
		# Ingredients
		jsonText += '\"ingredients\":['
		for i in self.ingredients:
			jsonText += '\"' + i + '\",'
		jsonText = jsonText[:-1]
		jsonText += ']'
		jsonText += ','
		# Now add the steps to create
		jsonText += '\"steps\":['
		for s in self.steps:
			jsonText += '\"' + s + '\",'
		jsonText = jsonText[:-1]
		jsonText += ']'
		jsonText += '}'
		# jsonText += ''
		# jsonText += ''
		return jsonText

