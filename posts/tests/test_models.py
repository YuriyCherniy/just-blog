from django.test import TestCase
from django.urls import reverse

from posts.models import Image, Post, PostAbout


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


class PostAboutModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        PostAbout.objects.create(title='post about', text='some text')

    def test_post_about_model_str_method(self):
        post_about = PostAbout.objects.first()
        str_method_result = post_about.__str__()
        self.assertEqual(str_method_result, post_about.title)


class ImageModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        post = Post.objects.create(
            title='test title', slug='test-slug', text='test text',
        )
        Image.objects.create(image='fake-url', post=post)

    def test_image_model_str_method(self):
        image = Image.objects.first()
        str_method_result = image.__str__()
        self.assertEqual(str_method_result, f'изображение №{image.pk}')

    def test_get_image_url_method(self):
        image = Image.objects.first()
        url = image.get_image_url()
        self.assertEqual(url, f'<h3>{image.image.url}</h3>')

    def test_get_image_method(self):
        image = Image.objects.first()
        img_tag = image.get_image_tag()
        self.assertEqual(img_tag, f'<img src="{image.image.url}" width="150" height="auto"/>')
