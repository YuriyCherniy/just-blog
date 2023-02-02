from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Post, PostAbout
from tags.models import Tag


class PostViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title='test title', slug='test-title', text='some test text'
        )
        PostAbout.objects.create(
            title='about title', text='some text'
        )

    def setUp(self):
        self.c = Client()

    # status code 200
    def test_post_detail_view_status_code_200(self):
        post = Post.objects.first()
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_about_view_status_code_200(self):
        response = self.c.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # template used
    def test_post_detail_template_used(self):
        post = Post.objects.first()
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_post_detail_about_template_used(self):
        response = self.c.get(reverse('about'))
        self.assertTemplateUsed(response, 'posts/post_detail_about.html')

    # other tests
    def test_post_detail_view_get_context_data_method(self):
        post = Post.objects.first()
        tag = Tag.objects.create(title='test title', slug='test-title')
        post.tag.set([tag])
        response = self.c.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(len(response.context['tag_list']), 1)

    def test_post_detail_about_get_object_method(self):
        post_about = PostAbout.objects.first()
        response = self.c.get(reverse('about'))
        self.assertEqual(response.context['object'], post_about)
