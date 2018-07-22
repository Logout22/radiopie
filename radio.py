#!  /usr/bin/env python3
""" Navigate through radio stations """

import unittest

class TestRadio(unittest.TestCase):
    def setUp(self):
        self.config = {'last_station': 1}
        self.radio = Radio(self.config, 3)

    def test_play_last_station(self):
        expected_index = 1
        self._verify_station(expected_index)

    def test_play_next_station(self):
        expected_new_index = 2
        self.radio.select_next_station()
        self._verify_station(expected_new_index)

    def test_play_previous_station(self):
        expected_new_index = 0
        self.radio.select_previous_station()
        self._verify_station(expected_new_index)

    def _verify_station(self, expected_new_index):
        self.assertEqual(expected_new_index, self.config['last_station'])

class Radio(object):
    """ Controls radio playback """
    def __init__(self, config, station_count):
        self._station_count = 0
        self._config = config
        self._station_count = station_count

    def get_current_station(self):
        """ Return the station that currently plays. """
        return self._config['last_station']

    def select_next_station(self):
        """ Select the next station among the array of stations given at construction. """
        self._config['last_station'] = (self._config['last_station'] + 1) % self._station_count

    def select_previous_station(self):
        """ Select the previous station among the array of stations given at construction. """
        self._config['last_station'] = (self._config['last_station'] - 1) % self._station_count

if __name__ == '__main__':
    unittest.main()
