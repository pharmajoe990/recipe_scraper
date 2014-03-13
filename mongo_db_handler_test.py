#! /usr/bin/env python

from mongo_db_handler import *

import unittest

class MongoHandlerTest(unittest.TestCase):
	"""Tests for the MongoHandler class"""
	
	def test_connect_to_database(self):
		handler = MongoHandler('localhost', 27107)
		self.assertTrue(handler.isConnected())