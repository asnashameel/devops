import unittest
from unittest.mock import patch
import requests

def get_data_from_api():
    """Fetches data from an external API (Simulating real behavior)"""
    response = requests.get("https://api.example.com/data")
    return response.json()


class TestAPIData(unittest.TestCase):
    @patch("__main__.get_data_from_api")  # Mock the function
    def test_get_data_mocked(self, mock_get_data):
        # Define the mock return value
        mock_get_data.return_value = {"id": 1, "name": "Mock User"}

        # Call the function (it will use the mock instead of the real function)
        result = get_data_from_api()

        # Verify the mocked function was called
        mock_get_data.assert_called_once()

        # Check if the returned data matches our mock
        self.assertEqual(result, {"id": 1, "name": "Mock User"})

if __name__ == "__main__":
    unittest.main()
