from django.test import TestCase, Client
from django.urls import reverse
from django.db import transaction, IntegrityError

from guestroom.services import NewGuestPostCounter
from users.models import BlogUser
from guestroom.models import GuestPost, GuestComment


class GuestPostListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user',
            password='0000'
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200(self):
        response = self.c.get(reverse('guest_room'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.c.get(reverse('guest_room'))
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_reset_guest_post_counter(self):
        counter = NewGuestPostCounter()
        counter.add_one()
        self.c.login(username='s_user', password='0000')
        self.c.get(reverse('guest_room'))
        self.assertEqual(counter.get_counter(), 0)


class GuestPostDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user',
            password='0000'
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_403(self):
        response = self.c.get(reverse('guest_post_detail', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_status_code_200(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym',
            text='Some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym',
            text='Some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_post_detail', args=[post.pk]))
        self.assertTemplateUsed(response, 'guestroom/guestpost_detail.html')


class GuestPostCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user',
            password='0000'
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200_get(self):
        response = self.c.get(reverse('guest_post_create'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_200_post(self):
        response = self.c.post(
            reverse('guest_post_create'),
            {'anonymous_username': 'anonym', 'text': 'some text'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_template_used_post_valid_data(self):
        response = self.c.post(
            reverse('guest_post_create'),
            {'anonymous_username': 'anonym', 'text': 'some text'},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_template_used_post_invalid_data(self):
        response = self.c.post(
            reverse('guest_post_create'),
            {'anonymous_username': '', 'text': ''},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_form.html')

    def test_post_counter(self):
        counter = NewGuestPostCounter()
        self.c.post(
            reverse('guest_post_create'),
            {'anonymous_username': 'anonym', 'text': 'some text'},
            follow=True
        )
        self.assertEqual(counter.get_counter(), 1)


class GuestPostUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user',
            password='0000'
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200_get(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_post_update', args=[post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_status_code_200_post(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.post(
            reverse('guest_post_update', args=[post.pk]),
            {'anonymous_username': 'anonym', 'text': 'some text'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_status_code_403(self):
        response = self.c.get(reverse('guest_post_update', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_template_used_post_valid_data(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.post(
            reverse('guest_post_update', args=[post.pk]),
            {'anonymous_username': 'anonym', 'text': 'some text'},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_template_used_post_invalid_data(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.post(
            reverse('guest_post_update', args=[post.pk]),
            {'anonymous_username': '', 'text': ''},
            follow=True
        )
        self.assertTemplateUsed(
            response, 'guestroom/guestpost_update_form.html'
        )


class GuestPostDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(username='s_user', password='0000')

    def setUp(self):
        self.c = Client()

    def test_status_code_200(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.delete(
            reverse('guest_post_delete', args=[post.pk]), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_status_code_403(self):
        response = self.c.delete(reverse('guest_post_delete', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_template_used_delete(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.delete(
            reverse('guest_post_delete', args=[post.pk]), follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_template_used_get(self):
        post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        self.c.login(username='s_user', password='0000')
        response = self.c.get(
            reverse('guest_post_delete', args=[post.pk]), follow=True
        )
        self.assertTemplateUsed(
            response, 'guestroom/guestpost_confirm_delete.html'
        )


class GuestCommentCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(username='s_user', password='0000')

        GuestPost.objects.create(
            anonymous_username='anonym',
            text='some text'
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200(self):
        self.c.login(username='s_user', password='0000')
        response = self.c.post(reverse('guest_comment_create'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_403(self):
        response = self.c.post(reverse('guest_comment_create'))
        self.assertEqual(response.status_code, 403)

    def test_guest_comment_create_valid_data(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        self.c.post(
            reverse('guest_comment_create'),
            {'username': 's_user', 'text': 'some text', 'guest_post_pk': guest_post.pk}
        )
        guest_comments = GuestComment.objects.all()
        self.assertEqual(len(guest_comments), 1)

    def test_guest_comment_create_valid_data_template_used(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        response = self.c.post(
            reverse('guest_comment_create'),
            {'username': 's_user', 'text': 'some text', 'guest_post_pk': guest_post.pk},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_guest_comment_create_invalid_data(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        self.c.post(
            reverse('guest_comment_create'),
            {'username': '', 'text': '', 'guest_post_pk': guest_post.pk}
        )
        guest_comments = GuestComment.objects.all()
        self.assertEqual(len(guest_comments), 0)

    def test_guest_comment_create_invalid_data_template_used(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        response = self.c.post(
            reverse('guest_comment_create'),
            {'username': '', 'text': '', 'guest_post_pk': guest_post.pk},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestcomment_form.html')

    def test_guest_comment_create_comment_already_exists(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        self.c.post(
            reverse('guest_comment_create'),
            {'username': 's_user', 'text': 'some text', 'guest_post_pk': guest_post.pk}
        )
        try:
            with transaction.atomic():
                self.c.post(
                    reverse('guest_comment_create'),
                    {'username': 's_user', 'text': 'new text', 'guest_post_pk': guest_post.pk}
                )
        except IntegrityError:
            pass
        guest_comments = GuestComment.objects.all()
        self.assertEqual(len(guest_comments), 1)

    def test_guest_comment_create_comment_already_exists_status_code_302(self):
        self.c.login(username='s_user', password='0000')
        guest_post = GuestPost.objects.first()
        self.c.post(
            reverse('guest_comment_create'),
            {'username': 's_user', 'text': 'some text', 'guest_post_pk': guest_post.pk}
        )
        try:
            with transaction.atomic():
                response = self.c.post(
                    reverse('guest_comment_create'),
                    {'username': 's_user', 'text': 'new text', 'guest_post_pk': guest_post.pk},
                )
        except IntegrityError:
            pass
        self.assertEqual(response.status_code, 302)


class GuestCommentUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user', password='0000'
        )
        guest_post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        GuestComment.objects.create(
            username='s_user',
            text='some text',
            guest_post=guest_post
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_comment_update', args=[post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_status_code_403(self):
        response = self.c.get(reverse('guest_comment_update', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_template_used_get(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_comment_update', args=[post.pk]))
        self.assertTemplateUsed(
            response, 'guestroom/guestcomment_update_form.html'
        )

    def test_template_used_post_valid_data(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.post(
            reverse('guest_comment_update', args=[post.pk]),
            {'username': 's_user', 'text': 'new text'},
            follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')

    def test_template_used_post_invalid_data(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.post(
            reverse('guest_comment_update', args=[post.pk]),
            {'username': '', 'text': ''},
            follow=True
        )
        self.assertTemplateUsed(
            response, 'guestroom/guestcomment_update_form.html'
        )


class GuestCommentDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BlogUser.objects.create_superuser(
            username='s_user', password='0000'
        )
        guest_post = GuestPost.objects.create(
            anonymous_username='anonym', text='some text'
        )
        GuestComment.objects.create(
            username='s_user',
            text='some text',
            guest_post=guest_post
        )

    def setUp(self):
        self.c = Client()

    def test_status_code_200_get(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.get(reverse('guest_comment_delete', args=[post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_status_code_200_delete(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.delete(
            reverse('guest_comment_delete', args=[post.pk]), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_status_code_403_get(self):
        response = self.c.get(reverse('guest_comment_delete', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_status_code_403_delete(self):
        response = self.c.delete(reverse('guest_comment_delete', args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_template_used_get(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.get(
            reverse('guest_comment_delete', args=[post.pk]), follow=True
        )
        self.assertTemplateUsed(
            response, 'guestroom/guestcomment_confirm_delete.html'
        )

    def test_template_used_delete(self):
        post = GuestComment.objects.first()
        self.c.login(username='s_user', password='0000')
        response = self.c.delete(
            reverse('guest_comment_delete', args=[post.pk]), follow=True
        )
        self.assertTemplateUsed(response, 'guestroom/guestpost_list.html')
