from django.test import SimpleTestCase
from django.urls import reverse, resolve

from posts.views import PostDetail


class PostUrlsTestCase(SimpleTestCase):
    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail', args=['test-slug'])
        view = resolve(url).func.view_class
        self.assertEqual(view, PostDetail)
