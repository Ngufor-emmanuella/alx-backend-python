import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=unittest.mock.PropertyMock) as mock_url:
            mock_url.return_value = "http://fake-url.com"

            client = GithubOrgClient("any_org")
            repos = client.public_repos

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://fake-url.com")
