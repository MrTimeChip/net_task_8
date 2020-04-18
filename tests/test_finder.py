import unittest
from finder import Finder
from API import API


class FinderTest(unittest.TestCase):
    def test_finder_should_find_friends_intersection(self):
        api = API(
            'efc4caa9efc4caa9efc4caa9b0efb5edf4eefc4efc4caa9b15db1196157aab3aea11d11',
            '5.103')
        finder = Finder(api)
        intersection = finder.find_friends_intersection('1', '1')
        actual_friends = api.get_friends('1', {'fields': 'name'})['response']['items']
        self.assertEqual(len(intersection), len(actual_friends))