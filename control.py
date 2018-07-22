#!  /usr/bin/env python3
""" Control radio components from interface """
import unittest

from fakeplayer import FakePlayer
from fakescreen import FakeScreen
from radio import Radio

class TestControl(unittest.TestCase):
    def setUp(self):
        self.stations = [
            {'name': 'station1', 'content': {'url': 'http://example.com'}},
            {'name': 'station2', 'content': {'url': 'http://example.org'}},
            {'name': 'station3', 'content': {'url': 'http://example.net'}}
            ]
        self.player = FakePlayer()
        self.screen = FakeScreen()
        self.radio = Radio({'last_station': 1}, 3)
        self.control = Control(self.stations, self.player, self.screen, self.radio)

    def test_show_playing_station(self):
        self._verify_station(self.stations[1])

    def test_show_playing_song(self):
        self.player.set_media_info_consumer(self.control)
        self.assertEqual(self.player.get_current_song(), self.screen.get_line(1))

    def test_next_station(self):
        self.control.next_button_pressed()
        self._verify_station(self.stations[2])

    def test_previous_station(self):
        self.control.previous_button_pressed()
        self._verify_station(self.stations[0])

    def _verify_station(self, expected_station):
        self.assertEqual(expected_station['content']['url'], self.player.get_last_url())
        self.assertEqual(expected_station['name'], self.screen.get_line(0))

class Control(object):
    """ Control the radio unit """
    def __init__(self, stations, media_player, screen, radio):
        self._current_radio_station = {}
        self._stations = stations
        self._media_player = media_player
        self._screen = screen
        self._radio = radio

        self._switch_station()

    def _switch_station(self):
        self._update_current_station()
        self._invoke_media_player()
        self._update_screen()

    def _update_current_station(self):
        self._current_radio_station = self._stations[self._radio.get_current_station()]

    def _invoke_media_player(self):
        self._media_player.play_url(self._current_radio_station['content']['url'])

    def _update_screen(self):
        self._screen.set_line(0, self._current_radio_station['name'])

    def report_new_song(self, title):
        """ Show new song on screen """
        self._screen.set_line(1, title)

    def next_button_pressed(self):
        """ React on "Next" button press """
        self._radio.select_next_station()
        self._switch_station()

    def previous_button_pressed(self):
        """ React on "Previous" button press """
        self._radio.select_previous_station()
        self._switch_station()

if __name__ == '__main__':
    unittest.main()
