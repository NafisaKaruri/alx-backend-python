#!/usr/bin/env python3
"""
Test clients.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that org method returns correctly"""
        test_class = GithubOrgClient(input)
        test_class.org()

        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
