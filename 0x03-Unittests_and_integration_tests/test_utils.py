import unittest
from unittest.mock import patch
from client import GithubOrgClient  # Adjust the import based on your project structure

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL based on the mocked payload."""
        
        # Set up the mock return value for org
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }
        
        # Create an instance of GithubOrgClient
        client = GithubOrgClient('google')
        
        # Access the _public_repos_url property
        result = client._public_repos_url
        
        # Check that the result is as expected
        self.assertEqual(result, 'https://api.github.com/orgs/google/repos')

if __name__ == '__main__':
    unittest.main()