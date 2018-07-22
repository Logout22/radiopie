#!  /usr/bin/env python3
""" Navigate through radio stations and trigger playback """

from random import randint
import unittest

class TestRadio(unittest.TestCase):
    def setUp(self):
        self.general = {'name': 'general', 'content': {'last_station': 1}}
        self.stations = [
            {'name': 'station1', 'content': {'url': 'http://example.com'}},
            {'name': 'station2', 'content': {'url': 'http://example.org'}},
            {'name': 'station3', 'content': {'url': 'http://example.net'}}
            ]
        config = self.stations[:]
        config.insert(randint(0, 3), self.general)
        self.radio = Radio(config)

    def test_play_last_station(self):
        self.assertEqual('station2', self.radio.get_current_station()['name'])

    def test_play_next_station(self):
        expected_new_index = 2
        self.radio.select_next_station()
        self._verify_station_switched(expected_new_index)

    def test_play_previous_station(self):
        expected_new_index = 0
        self.radio.select_previous_station()
        self._verify_station_switched(expected_new_index)

    def _verify_station_switched(self, expected_new_index):
        expected_station = self.stations[expected_new_index]
        self.assertEqual(expected_station['name'], self.radio.get_current_station()['name'])
        self.assertEqual(expected_new_index, self.general['content']['last_station'])

class Radio(object):
    """ Controls radio playback """
    def __init__(self, config):
        self._stations = []
        self._load_config(config)

    def get_current_station(self):
        """ Return an object describing the station that currently plays. """
        return self._stations[self._general['last_station']]

    def select_next_station(self):
        """ Select the next station in the array of stations given at construction. """
        self._general['last_station'] = (self._general['last_station'] + 1) % len(self._stations)

    def select_previous_station(self):
        """ Select the previous station in the array of stations given at construction. """
        self._general['last_station'] = (self._general['last_station'] - 1) % len(self._stations)

    def _load_config(self, config):
        for section in config:
            if section['name'] == 'general':
                self._general = section['content']
            else:
                self._stations.append(section)

if __name__ == '__main__':
    unittest.main()
