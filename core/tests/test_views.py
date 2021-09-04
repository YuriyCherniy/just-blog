from django.test import TestCase, Client, SimpleTestCase

from posts.models import Post
from core.views import IndexView


class CoreViewsTesCase(TestCase):
    def setUp(self):
        self.c = Client()

    # status code 200
    def test_index_view_status_code_200(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # template used
    def test_index_view_template_used(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'core/index.html')

    def test_index_view_get_queryset_method(self):
        Post.objects.create(title='t_1', slug='s-1', text='txt', is_published=True)
        Post.objects.create(title='t_2', slug='s-2', text='txt', is_published=False)
        Post.objects.create(title='t_3', slug='s-3', text='txt', is_published=True)
        view = IndexView()
        self.assertEqual(len(view.get_queryset()), 2)


class RobotsTxtTestCase(SimpleTestCase):
    def setUp(self):
        self.c = Client()

    def test_robots_txt_view_template_used(self):
        response = self.c.get('/robots.txt')
        self.assertTemplateUsed(response, 'core/robots.txt')

    def test_robots_txt_view_status_code_200(self):
        response = self.c.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
