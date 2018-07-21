#!  /usr/bin/env python3
""" Navigate through radio stations and trigger playback """

from random import randint
import unittest

class TestRadio(unittest.TestCase):
    class FakePlayer(object):
        """ Fake media player class which captures function call from Radio """
        def __init__(self):
            self._last_url = ""

        def play_url(self, url):
            self._last_url = url

        def get_last_url(self):
            return self._last_url

    def setUp(self):
        self.general = {'name': 'general', 'content': {'last_station': 1}}
        self.stations = [
            {'name': 'station1', 'content': {'url': 'http://example.com'}},
            {'name': 'station2', 'content': {'url': 'http://example.org'}},
            {'name': 'station3', 'content': {'url': 'http://example.net'}}
            ]
        self.player = self.FakePlayer()
        config = self.stations[:]
        config.insert(randint(0, 3), self.general)
        self.radio = Radio(config, self.player)

    def test_play_last_station(self):
        self.assertEqual('station2', self.radio.get_playing_station()['name'])
        self.assertEqual('http://example.org', self.player.get_last_url())

    def test_play_next_station(self):
        expected_new_index = 2
        self.radio.play_next_station()
        self._verify_station_switched(expected_new_index)

    def test_play_previous_station(self):
        expected_new_index = 0
        self.radio.play_previous_station()
        self._verify_station_switched(expected_new_index)

    def _verify_station_switched(self, expected_new_index):
        expected_station = self.stations[expected_new_index]
        self.assertEqual(expected_station['name'], self.radio.get_playing_station()['name'])
        self.assertEqual(expected_new_index, self.general['content']['last_station'])
        self.assertEqual(expected_station['content']['url'], self.player.get_last_url())

class Radio(object):
    """ Control the radio unit """
    def __init__(self, config, media_player):
        self._stations = []
        self._load_config(config)
        self._media_player = media_player
        self._invoke_media_player()

    def get_playing_station(self):
        """ Return an object describing the station that currently plays. """
        return self._stations[self._general['last_station']]

    def play_next_station(self):
        """ Play the next station in the array of stations given at construction. """
        self._select_next_station()
        self._invoke_media_player()

    def play_previous_station(self):
        """ Play the next station in the array of stations given at construction. """
        self._select_previous_station()
        self._invoke_media_player()

    def _load_config(self, config):
        for section in config:
            if section['name'] == 'general':
                self._general = section['content']
            else:
                self._stations.append(section)

    def _select_next_station(self):
        self._general['last_station'] = (self._general['last_station'] + 1) % len(self._stations)

    def _select_previous_station(self):
        self._general['last_station'] = (self._general['last_station'] - 1) % len(self._stations)

    def _invoke_media_player(self):
        self._media_player.play_url(self.get_playing_station()['content']['url'])

if __name__ == '__main__':
    unittest.main()
