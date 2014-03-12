#! /usr/bin/env python

# Handle various database operations for mongoDB interaction

from pymongo import MongoClient

conn = None

class MongoHandler(object):
	"""Handles various functions related to mongoDB"""
	def __init__(self, host_name, port, collection):
		conn = Database(MongoClient(host_name, port), collection)
