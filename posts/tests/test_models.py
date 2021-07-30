from django.test import TestCase
from django.urls import reverse

from posts.models import Post, PostAbout


class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='test title', slug='test-slug', text='test text',
        )
        PostAbout.objects.create(title='post about', text='some text')

    def test_post_model_str_method(self):
        post = Post.objects.first()
        str_method_result = post.__str__()
        self.assertEqual(str_method_result, post.title)

    def test_post_model_get_absolute_url_method(self):
        post = Post.objects.first()
        url = reverse('post_detail', args=[post.slug])
        absolute_url = post.get_absolute_url()
        self.assertEqual(absolute_url, url)

    def test_post_about_model_str_method(self):
        post_about = PostAbout.objects.first()
        str_method_result = post_about.__str__()
        self.assertEqual(str_method_result, post_about.title)
