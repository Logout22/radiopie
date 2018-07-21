#!  /usr/bin/env python3
""" Navigate through radio stations and trigger playback """

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
        self.stations = [
            {'name': 'general', 'content': {'last_station': 2}},
            {'name': 'station1', 'content': {'url': 'http://example.com'}},
            {'name': 'station2', 'content': {'url': 'http://example.org'}},
            {'name': 'station3', 'content': {'url': 'http://example.net'}}
            ]
        self.player = self.FakePlayer()
        self.radio = Radio(self.stations, self.player)

    def test_play_last_station(self):
        self.assertEqual('station2', self.radio.get_playing_station()['name'])
        self.assertEqual('http://example.org', self.player.get_last_url())

    def test_play_next_station(self):
        new_stations = self.radio.play_next_station()
        self.assertEqual('station3', self.radio.get_playing_station()['name'])
        self.assertEqual(new_stations[0]['content']['last_station'], 3)
        self.assertEqual('http://example.net', self.player.get_last_url())

    def test_play_previous_station(self):
        new_stations = self.radio.play_previous_station()
        self.assertEqual('station1', self.radio.get_playing_station()['name'])
        self.assertEqual(new_stations[0]['content']['last_station'], 1)
        self.assertEqual('http://example.com', self.player.get_last_url())

class Radio(object):
    """ Control the radio unit """
    def __init__(self, stations, media_player):
        self._stations = stations
        self._playing_station = self._stations[0]['content']['last_station']
        self._media_player = media_player
        self._invoke_media_player()

    def get_playing_station(self):
        """ Return an object describing the station that currently plays. """
        return self._stations[self._playing_station]

    def play_next_station(self):
        """ Play the next station in the array of stations given at construction. """
        self._select_next_station()
        self._invoke_media_player()
        self._update_last_station()
        return self._stations

    def play_previous_station(self):
        """ Play the next station in the array of stations given at construction. """
        self._select_previous_station()
        self._invoke_media_player()
        self._update_last_station()
        return self._stations

    def _select_next_station(self):
        self._playing_station = (self._playing_station + 1) % len(self._stations)

    def _select_previous_station(self):
        self._playing_station = (self._playing_station - 1) % len(self._stations)

    def _update_last_station(self):
        self._stations[0]['content']['last_station'] = self._playing_station

    def _invoke_media_player(self):
        self._media_player.play_url(self._stations[self._playing_station]['content']['url'])

if __name__ == '__main__':
    unittest.main()
