import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Adjust the import based on your project structure

class TestGithubOrgClient(unittest.TestCase):
    
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Set up the mock return value
        mock_get_json.return_value = {'login': org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Ensure get_json was called once with the expected argument
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
        # Assert that the returned value is what we expect
        self.assertEqual(result, {'login': org_name})

if __name__ == '__main__':
    unittest.main()