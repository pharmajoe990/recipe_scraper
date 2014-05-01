from scraper.TasteDotCom import TasteDotCom
from scraper.TasteDotComStatic import TasteDotComStatic

__author__ = 'tim'

import unittest


class RecipeParserTest(unittest.TestCase):
    def test_parse_from_static_page(self):
        test_page = '../miscellany/sausage_and_punpkin_curry.html'
        taste_page = TasteDotComStatic(test_page)

        self.assertEqual(taste_page.title, 'Sausage and pumpkin curry')
        self.assertEqual(taste_page.summary, 'Whip up a delicious and budget friendly meal with this delicious sausage '
                                             'and pumpkin curry recipe.')
        self.assertEqual(taste_page.prep_time, '0:20')
        self.assertEqual(len(taste_page.ingredients), 10)
        self.assertEqual(len(taste_page.steps), 3)

    def test_parse_from_page(self):
        test_page = 'http://www.taste.com.au/recipes/22279/sausage+and+pumpkin+curry'
        taste_page = TasteDotCom(test_page)

        self.assertEqual(taste_page.title, 'Sausage and pumpkin curry')
        self.assertEqual(taste_page.summary, 'Whip up a delicious and budget friendly meal with this delicious sausage '
                                             'and pumpkin curry recipe.')
        self.assertEqual(taste_page.prep_time, '0:20')
        self.assertEqual(len(taste_page.ingredients), 10)
        self.assertEqual(len(taste_page.steps), 3)