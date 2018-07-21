#!  /usr/bin/env python3
""" Navigate through radio stations and trigger playback """

import unittest

class TestRadio(unittest.TestCase):
    def setUp(self):
        self.stations = [
            {'name': 'general', 'content': {'last_station': 2}},
            {'name': 'station1', 'content': {'url': 'http://example.com'}},
            {'name': 'station2', 'content': {'url': 'http://example.org'}},
            {'name': 'station3', 'content': {'url': 'http://example.net'}}
            ]
        self.radio = Radio(self.stations)

    def test_play_last_station(self):
        self.assertEqual('station2', self.radio.get_playing_station()['name'])

    def test_play_next_station(self):
        self.radio.play_next_station()
        self.assertEqual('station3', self.radio.get_playing_station()['name'])

    def test_play_previous_station(self):
        self.radio.play_previous_station()
        self.assertEqual('station1', self.radio.get_playing_station()['name'])

class Radio(object):
    """ Control the radio unit """
    def __init__(self, stations):
        self.stations = stations
        self.playing_station = stations[0]['content']['last_station']

    def get_playing_station(self):
        """ Return an object describing the station that currently plays. """
        return self.stations[self.playing_station]

    def play_next_station(self):
        """ Play the next station in the array of stations given at construction. """
        self.playing_station = (self.playing_station + 1) % len(self.stations)

    def play_previous_station(self):
        """ Play the next station in the array of stations given at construction. """
        self.playing_station = (self.playing_station - 1) % len(self.stations)

if __name__ == '__main__':
    unittest.main()
