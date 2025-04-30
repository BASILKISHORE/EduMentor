"""
Unit tests for EduMentor application with Azure simulation.
"""

import unittest
from unittest.mock import patch, AsyncMock
from app import call_azure_function

class TestEduMentor(unittest.TestCase):
    @patch("app.requests.post")
    def test_call_azure_function_success(self, mock_post):
        """Test successful Azure Function call."""
        mock_post.return_value = AsyncMock(status_code=200, json=AsyncMock(return_value={"content": ["Sample data"]}))
        result = call_azure_function("testFunction", {"key": "value"})
        self.assertEqual(result, {"content": ["Sample data"]})

    @patch("app.requests.post")
    def test_call_azure_function_error(self, mock_post):
        """Test Azure Function call with error."""
        mock_post.side_effect = requests.exceptions.RequestException("Error")
        result = call_azure_function("testFunction", {"key": "value"})
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()