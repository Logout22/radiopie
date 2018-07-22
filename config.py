#!  /usr/bin/env python3
""" Load the configuration file """

import configparser
import unittest

class TestConfig(unittest.TestCase):
    def test_load_station(self):
        expected_key = "test1"
        expected_value = "testvalue1"
        expected_station = 'teststation'
        expected_url = 'http://example.com'
        stations_file = '[general]\n{}={}\n[{}]\nurl={}'\
                .format(expected_key, expected_value, expected_station, expected_url)
        config = load_config(stations_file)
        self.assertEqual(expected_value, config['general'][expected_key])
        self.assertEqual(expected_station, config['stations'][0]['name'])
        self.assertEqual(expected_url, config['stations'][0]['content']['url'])

    def test_store_station(self):
        expected_general_section = '[general]\ntest1 = testvalue1'
        expected_station_section = '[teststation]\nurl = http://example.com\n\n'

        stations = [{'name': 'teststation', 'content': {'url': 'http://example.com'}}]
        configuration = {'general': {'test1': 'testvalue1'}, 'stations': stations}
        file_content = store_config(configuration)
        self.assertTrue(expected_general_section in file_content)
        self.assertTrue(expected_station_section in file_content)

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

def load_config(file_content):
    """ Load radio stations from a given configuration string """
    parser = configparser.ConfigParser()
    parser.read_string(file_content)
    configuration = {}
    configuration['stations'] = []
    for section in parser.sections():
        content = dict(parser.items(section))
        if section == 'general':
            configuration['general'] = content
        else:
            configuration['stations'].append({'name':section, 'content':content})
    return configuration

def store_config(configuration):
    """ Create a configuration string from a given stations object """
    parser = configparser.ConfigParser()
    parser['general'] = configuration['general']
    for station in configuration['stations']:
        parser[station['name']] = station['content']
    fake_file = FakeFile()
    parser.write(fake_file)
    return fake_file.get_text()

if __name__ == '__main__':
    unittest.main()
