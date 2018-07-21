#!  /usr/bin/env python3
""" Fake media playback for testing the radio """

class FakePlayer(object):
    """ Fake media player class which captures function calls from Radio """
    def __init__(self):
        self._last_url = ""

    def play_url(self, url):
        print('Now playing ', url)
        self._last_url = url

    def get_last_url(self):
        return self._last_url
