from django.test import TestCase

from posts.models import Post

from posts.templatetags.get_random_posts_tag import show_random_recommended_posts


class RandomPostsTestCase(TestCase):
    def setUp(self):
        for i in range(1, 4):
                    Post.objects.create(
            title=f'published title {i}', slug=f'test-title-{i}', text=f'some test text {i}', is_published=True
        )

        Post.objects.create(
            title='not published title', slug='test-title', text='some test text'
        )


    def test_show_random_recommended_posts_function(self):
        post = Post.objects.get(title='published title 1')
        random_posts = show_random_recommended_posts(post.pk)
        returned_posts_number = len(random_posts.get('random_posts'))
        self.assertEqual(returned_posts_number, 2)
