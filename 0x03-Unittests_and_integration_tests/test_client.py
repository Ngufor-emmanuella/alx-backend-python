import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        with patch.object(GithubOrgClient, "org", new_callable=unittest.mock.PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://fake-url.com"}
            client = GithubOrgClient("any_org")
            self.assertEqual(client._public_repos_url, "http://fake-url.com")
