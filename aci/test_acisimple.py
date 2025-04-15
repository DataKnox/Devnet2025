import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aci.acisimple import get_token, get_tenants

class TestACISimple(unittest.TestCase):
    def setUp(self):
        self.url = "https://sandboxapicdc.cisco.com"
        self.username = "admin"
        self.password = "!v3G@!4@Y"
        self.token = "test_token"

    @patch('aci.acisimple.requests.post')
    def test_get_token_success(self, mock_post):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "imdata": [{
                "aaaLogin": {
                    "attributes": {
                        "token": self.token
                    }
                }
            }]
        }
        mock_post.return_value = mock_response

        result = get_token(self.url, self.username, self.password)
        self.assertEqual(result, self.token)
        mock_post.assert_called_once()

    @patch('aci.acisimple.requests.post')
    def test_get_token_failure(self, mock_post):
        # Mock failed response
        mock_post.side_effect = Exception("Connection error")

        result = get_token(self.url, self.username, self.password)
        self.assertIsNone(result)

    @patch('aci.acisimple.requests.get')
    def test_get_tenants_success(self, mock_get):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "imdata": [
                {"fvTenant": {"attributes": {"name": "tenant1"}}},
                {"fvTenant": {"attributes": {"name": "tenant2"}}}
            ]
        }
        mock_get.return_value = mock_response

        result = get_tenants(self.url, self.token)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["fvTenant"]["attributes"]["name"], "tenant1")
        mock_get.assert_called_once()

    @patch('aci.acisimple.requests.get')
    def test_get_tenants_failure(self, mock_get):
        # Mock failed response
        mock_get.side_effect = Exception("Connection error")

        result = get_tenants(self.url, self.token)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 