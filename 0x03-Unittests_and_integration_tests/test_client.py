import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            mock_response = MagicMock()
            if url == cls.org_payload['url']:
                mock_response.json.return_value = cls.org_payload
            elif url == cls.repos_payload[0]['url']:
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}
            return mock_response

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos
        self.assertEqual(repos, self.expected_repos)
        self.assertIn(self.apache2_repos, repos)
