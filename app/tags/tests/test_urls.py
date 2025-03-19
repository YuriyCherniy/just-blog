from django.test import SimpleTestCase
from django.urls import resolve, reverse

from tags.views import PostListFromTag


class TagUrlsTestCase(SimpleTestCase):
    def test_post_from_tag_is_resolved(self):
        url = reverse('post_from_tag', args=['test-slug'])
        view = resolve(url).func.view_class
        self.assertEqual(view, PostListFromTag)
