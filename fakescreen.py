#!  /usr/bin/env python3
""" Fake LCD screen for testing the radio """

class FakeScreen(object):
    """ Fake screen class which captures function calls from Radio """
    def __init__(self, linecount = 2):
        self._line = ["" for i in range(linecount)]

    def set_line(self, idx, content):
        print('Set line ', idx, ' to ', content)
        self._line[idx] = content

    def get_line(self, idx):
        return self._line[idx]
