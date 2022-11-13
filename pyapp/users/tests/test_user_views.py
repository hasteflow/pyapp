from django.test import TestCase
from http import HTTPStatus

"""
This file should also be refactored in multiple files if necesary
"""


class HomePageTest(TestCase):
    def test_homepage_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "users/homepage.html")


class SecretAreaPageTest(TestCase):
    def test_secret_area_view_redirects_anonymous_user(self):
        """
        Redirects to login page with a 302 http FOUND redirect
        """

        response = self.client.get("/secret-area/", follow=False)
        self.assertEquals(response.status_code, HTTPStatus.FOUND)

        response = self.client.get("/secret-area/", follow=True)
        self.assertEquals(response.request.get("PATH_INFO"), "/login/")
