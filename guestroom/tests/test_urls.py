from django.test import SimpleTestCase
from django.urls import reverse, resolve

from guestroom.views import (
    GuestPostList,
    GuestPostDetail,
    GuestPostCreate,
    GuestPostUpdate,
    GuestPostDelete,
    GuestCommentCreate,
    GuestCommentDelete,
    GuestCommentUpdate,
)


class GuestPostUrlsTestCase(SimpleTestCase):
    def test_guest_post_list_url_is_resolved(self):
        url = reverse('guest_room')
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestPostList)

    def test_guest_post_create_url_is_resolved(self):
        url = reverse('guest_post_create')
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestPostCreate)

    def test_guest_post_update_url_is_resolved(self):
        url = reverse('guest_post_update', args=[1])
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestPostUpdate)

    def test_guest_post_delete_url_is_resolved(self):
        url = reverse('guest_post_delete', args=[1])
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestPostDelete)

    def test_guest_post_detail_url_is_resolved(self):
        url = reverse('guest_post_detail', args=[1])
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestPostDetail)

    def test_guest_comment_create_url_is_resolved(self):
        url = reverse('guest_comment_create')
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestCommentCreate)

    def test_guest_comment_delete_url_is_resolved(self):
        url = reverse('guest_comment_delete', args=[1])
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestCommentDelete)

    def test_guest_comment_update_url_is_resolved(self):
        url = reverse('guest_comment_update', args=[1])
        view = resolve(url).func.view_class
        self.assertEqual(view, GuestCommentUpdate)
