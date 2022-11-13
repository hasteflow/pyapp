from django.test import TestCase
from users.forms import UserLoginForm


class UserLoginFormTest(TestCase):
    def test_form_input_has_placeholders(self):
        """
        Login form must have Username and Password placeholders
        """

        form = UserLoginForm()
        self.assertIn('placeholder="Username or Email"', form.as_p())
        self.assertIn('placeholder="Password"', form.as_p())

    def test_form_validation_for_blank_items(self):
        """
        Login with empty credentials will trigger validation errors
        """

        form = UserLoginForm()
        self.assertFalse(form.is_valid())

        for item in form.errors.values():
            self.assertIn("This field is required", item)
