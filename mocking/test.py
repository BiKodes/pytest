from importlib.resources import path
import unittest
from unittest.mock import patch, MagicMock

from main import add, get_joke, len_joke


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

 
class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'value':
            {
                'joke': 'jambo kenya'
            }
        }

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'jambo kenya')

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):

        mock_response = MagicMock(status_code = 403)
        mock_response.json.return_value = {
            'value':
            {
                'joke': 'jambo kenya'
            }
        }

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'No jokes')



if __name__ == '__main__':
    unittest.main()