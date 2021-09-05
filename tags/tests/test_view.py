from django.test  import TestCase, Client
from django.urls import reverse

from tags.models import Tag
from posts.models import Post


class PostListFromTagTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(title='test tag', slug='test-slug')

    def setUp(self):
        self.c = Client()

    # status code 200
    def test_post_list_from_tag_status_code_200(self):
        tag = Tag.objects.first()
        response = self.c.get(reverse('post_from_tag', args=[tag.slug]))
        self.assertEqual(response.status_code, 200)

    # template used
    def test_post_list_from_tag_template_used(self):
        tag = Tag.objects.first()
        response = self.c.get(reverse('post_from_tag', args=[tag.slug]))
        self.assertTemplateUsed(response, 'tags/tags_post_list.html')

    # other tests
    def test_post_list_from_tag_get_queryset_method(self):
        tag = Tag.objects.first()
        post = Post.objects.create(title='test title', slug='test-slug')
        post.tag.set([tag])
        response = self.c.get(reverse('post_from_tag', args=[tag.slug]))
        self.assertEqual((len(response.context['post_list'])), 1)

    def test_post_list_from_tag_get_context_data_method(self):
        tag = Tag.objects.first()
        response = self.c.get(reverse('post_from_tag', args=[tag.slug]))
        self.assertEqual(response.context['tag'], 'test-slug')
