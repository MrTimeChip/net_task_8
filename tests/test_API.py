import unittest
from API import API


class APITests(unittest.TestCase):
    def test_get_friends_should_return_friends(self):
        api = API(
            'efc4caa9efc4caa9efc4caa9b0efb5edf4eefc4efc4caa9b15db1196157aab3aea11d11',
            '5.103')
        result = api.get_friends('1', {'fields': 'name'})
        self.assertNotEqual(result['response']['items'], {},
                            msg='should contain users')
