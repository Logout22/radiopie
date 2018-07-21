#!  /usr/bin/env python3
""" Load radio stations from configuration file """

import configparser
import unittest

class TestStations(unittest.TestCase):
    def test_load_station_url(self):
        expected_station = 'teststation'
        expected_url = 'http://example.com'
        stations_file = '[{}]\nurl={}'.format(expected_station, expected_url)
        stations = load_stations(stations_file)
        self.assertEqual(expected_url, stations[expected_station]['url'])

def load_stations(configuration):
    """ Load radio stations from a given configuration file """
    parser = configparser.ConfigParser()
    parser.read_string(configuration)
    return {section : dict(parser.items(section)) for section in parser.sections()}

if __name__ == '__main__':
    unittest.main()
