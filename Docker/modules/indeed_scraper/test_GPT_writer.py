import unittest
from unittest.mock import patch
from indeed_scraper.GPT_writer import get_descriptions, striphtml


class TestScriptFunctions(unittest.TestCase):

    def test_get_descriptions(self):
        expected_descriptions = ['Description 1', 'Description 2']
        
        # Patching the open function to return a mock file
        with patch('builtins.open', unittest.mock.mock_open(read_data='[{"description": "Description 1"}, {"description": "Description 2"}]')):
            descriptions = get_descriptions()
            self.assertEqual(descriptions, expected_descriptions)

    def test_striphtml(self):
        input_text = '<p>This is <b>bold</b> text.</p>'
        expected_output = 'This is bold text.'
        output = striphtml(input_text)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()