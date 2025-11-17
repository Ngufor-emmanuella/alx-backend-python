import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            first_call = test_obj.a_property
            second_call = test_obj.a_property

            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)
            mock_method.assert_called_once()
