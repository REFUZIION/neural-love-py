import unittest
from unittest.mock import patch

from neural_love_api import *


class TestNeuralLoveAPI(unittest.TestCase):

    @patch('requests.post')
    def test_generate_art(self, mock_post):
        # Arrange
        api = NeuralLoveAPI('dummy_key')
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = 'success'

        # Act
        response = api.generate_art(prompt='a cat', style='painting', layout='square',
                                    amount=1, is_hd=False, is_public=True)

        # Assert
        self.assertEqual(response, 'success')


if __name__ == '__main__':
    unittest.main()
