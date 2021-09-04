from django.test import SimpleTestCase
from django.urls import resolve

from core.views import IndexView, RobotsTxt


class CoreUrlsTestCase(SimpleTestCase):
    def test_index_view_url_is_resolved(self):
        view = resolve('/').func.view_class
        self.assertEqual(view, IndexView)

    def test_robots_txt_view_is_resolved(self):
        view = resolve('/robots.txt').func.view_class
        self.assertEqual(view, RobotsTxt)
