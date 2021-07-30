from django.test import TestCase
from django.urls import reverse

from guestroom.models import GuestPost, GuestComment


class GuestPostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        GuestPost.objects.create(
            anonymous_username='anonimus',
            text='Some text'
        )
        GuestComment.objects.create(
            username='super_user',
            text='Some text' * 10,
            guest_post_id=1
        )

    def test_guest_post_model_str_method(self):
        post = GuestPost.objects.get(anonymous_username='anonimus')
        self.assertEqual(post.__str__(), post.anonymous_username)

    def test_get_absolute_url_method(self):
        post = GuestPost.objects.get(anonymous_username='anonimus')
        absolute_url = post.get_absolute_url()
        self.assertEqual(absolute_url, reverse('guest_post_detail', args=[post.pk]))

    def test_guest_comment_model_str_method(self):
        post = GuestComment.objects.get(username='super_user')
        self.assertEqual(post.__str__(), post.text[:40])
