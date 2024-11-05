#!/usr/bin/env python3
"""
Test clients.
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):

        """Test that result of _public_repos_url is the expected one based
        on the mocked payload."""
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
        ) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = {"repos_url": "World"}
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
