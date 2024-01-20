import unittest

from django.test import LiveServerTestCase
from selenium import webdriver


class TestLandingPage(LiveServerTestCase):
    """Test landing page can be called."""

    browser = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_server_starts_and_landing_page_is_up(self):
        """Verify that landing page can be reached on the server."""
        self.browser.get(f"{self.live_server_url}")
        self.assertIn("ESA3 CoachingIdeas", self.browser.title)


if __name__ == "__main__":
    unittest.main()
