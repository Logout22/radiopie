#!  /usr/bin/env python3
""" Load radio stations from configuration file """

import configparser
import unittest

class TestStations(unittest.TestCase):
    def test_load_station(self):
        expected_station = 'teststation'
        expected_url = 'http://example.com'
        stations_file = '[{}]\nurl={}'.format(expected_station, expected_url)
        stations = load_stations(stations_file)
        self.assertEqual(expected_station, stations[0]['name'])
        self.assertEqual(expected_url, stations[0]['content']['url'])

    def test_store_station(self):
        expected_string = '[teststation]\nurl = http://example.com\n\n'
        stations = [{'name': 'teststation', 'content': {'url': 'http://example.com'}}]
        self.assertEqual(expected_string, store_stations(stations))

class FakeFile(object):
    """ File adapter for config parser, which does not support string serialization """
    def __init__(self):
        self._text = ""

    def write(self, text_segment):
        """ Append text to the virtual file """
        self._text += text_segment

    def get_text(self):
        """ Retrieve the text gathered so far """
        return self._text

def load_stations(configuration):
    """ Load radio stations from a given configuration string """
    parser = configparser.ConfigParser()
    parser.read_string(configuration)
    return [{'name':section, 'content':dict(parser.items(section))}
            for section in parser.sections()]

def store_stations(stations):
    """ Create a configuration string from a given stations object """
    parser = configparser.ConfigParser()
    for section in stations:
        parser[section['name']] = section['content']
    fake_file = FakeFile()
    parser.write(fake_file)
    return fake_file.get_text()

if __name__ == '__main__':
    unittest.main()
