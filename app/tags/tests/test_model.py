from django.test import TestCase
from django.urls import reverse

from tags.models import Tag


class TagModelTastCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(title='test tag', slug='test-slug')

    def test_tag_model_str_method(self):
        tag = Tag.objects.first()
        str_result = tag.__str__()
        self.assertEqual(str_result, tag.title)

    def test_tag_model_get_absolute_url_method(self):
        tag = Tag.objects.first()
        url = tag.get_absolute_url()
        self.assertEqual(url, reverse('post_from_tag', args=[tag.slug]))