import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            mock_response = MagicMock()
            if url == f"https://api.github.com/orgs/{org_payload['login']}":
                mock_response.json.return_value = org_payload
            elif url == org_payload['repos_url']:
                mock_response.json.return_value = repos_payload
            else:
                mock_response.json.return_value = {}
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient(org_payload['login'])
        self.assertEqual(client.public_repos, expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient(org_payload['login'])
        filtered_repos = client.public_repos(license="apache-2.0")
        self.assertEqual(filtered_repos, apache2_repos)
