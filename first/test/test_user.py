import unittest

from first.src.user import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(first_name="Test", last_name="User", is_active=True, salary=101)
        self.inactive_user = User(first_name="", last_name="")

    def tearDown(self):
        self.user = None
        self.inactive_user = None

    def test_get_first_name_returns_name(self):
        self.assertEqual(self.user.get_first_name(), "Test")

    def test_get_first_name_raise_error(self):
        with self.assertRaises(ValueError):
            self.inactive_user.get_first_name()

    def test_get_last_name_raise_error(self):
        self.assertEqual(self.user.get_last_name(), "User")

    def test_get_last_name_returns_name(self):
        with self.assertRaises(ValueError):
            self.inactive_user.get_last_name()

    def test_user_is_active_returns_true(self):
        self.assertTrue(self.user.is_active)

    def test_user_is_inactive_returns_false(self):
        self.assertFalse(self.inactive_user.is_active)

    def test_user_is_rich_returns_proper_message(self):
        self.assertEqual(self.user.is_rich(), "user is rich")

    def test_inactive_user_is_poor_returns_proper_messagee(self):
        self.assertEqual(self.inactive_user.is_rich(), "user is poor")
