#!/usr/bin/env python3
"""
Tests utils.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function with parameterized inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
     ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Check if the exception was raised
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json returns expected results"""
        test_cases = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            mock = Mock()
            mock.json.return_value = test_payload
            mock_get.return_value = mock

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)

            mock_get.reset_mock()


if __name__ == '__main__':
    unittest.main()
