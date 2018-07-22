#!  /usr/bin/env python3
""" Fake media playback for testing the radio """

class FakePlayer(object):
    """ Fake media player class which captures function calls from Radio """
    def __init__(self):
        self._last_url = ""
        self._current_song = "Radio-Friendly Song"

    def play_url(self, url):
        print('Now playing ', url)
        self._last_url = url

    def get_last_url(self):
        return self._last_url

    def set_media_info_consumer(self, consumer):
        consumer.report_new_song(self._current_song)

    def get_current_song(self):
        return self._current_song
