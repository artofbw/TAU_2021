import unittest


class User:
    def __init__(self, first_name, last_name, is_active=False, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.salary = salary

    def get_first_name(self):
        if not self.first_name:
            raise ValueError("first name cannot be empty")
        return self.first_name

    def get_last_name(self):
        if not self.last_name:
            raise ValueError("last name cannot be empty")
        return self.last_name

    def is_rich(self):
        if self.salary > 100:
            return "user is rich"
        else:
            return "user is poor"


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


# if __name__ == '__main__':
#     user_test_case = UserTestCase()
#     user_test_case.run()
