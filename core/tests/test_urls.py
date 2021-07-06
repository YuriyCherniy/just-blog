from django.test import SimpleTestCase
from django.urls import resolve

from core.views import IndexView


class CoreUrlsTestCase(SimpleTestCase):
    def test_index_view_url_is_resolved(self):
        view = resolve('/').func.view_class
        self.assertEqual(view, IndexView)
