import unittest
from unittest.mock import patch
from tmclient.client import TMClient

class TestTMClient(unittest.TestCase):

    def setUp(self):
        self.client = TMClient(api_key="dummy_key", namespace="dummy_namespace")

    @patch('tmclient.client.requests.get')
    def test_get_data(self, mock_get):
        mock_get.return_value.json.return_value = {"status": "success"}
        mock_get.return_value.raise_for_status = lambda: None

        result = self.client.get_data()
        self.assertEqual(result, {"status": "success"})

if __name__ == '__main__':
    unittest.main()
