from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post
from tags.models import Tag


class PostViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='test title',
            slug='test-title',
            text='some test text'
        )

    def setUp(self):
        self.c = Client()

    # status code 200
    def test_post_detail_status_code_200(self):
        post = Post.objects.first()
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(response.status_code, 200)

    # template used
    def test_post_detail_template_used(self):
        post = Post.objects.first()
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    # other tests
    def test_post_detail_view_get_context_data_method(self):
        post = Post.objects.first()
        tag = Tag.objects.create(title='test title', slug='test-title')
        post.tag.set([tag])
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(len(response.context['tag_list']), 1)
