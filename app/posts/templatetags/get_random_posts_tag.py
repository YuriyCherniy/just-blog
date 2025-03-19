from django import template

from posts.models import Post

register = template.Library()


@register.inclusion_tag('posts/random_posts.html')
def show_random_recommended_posts(current_post_pk):
    '''
    Shows random posts under text of a post detail page
    '''
    random_posts = Post.objects.exclude(
        pk=current_post_pk
    ).exclude(
        is_published=False
    ).order_by('?')[:3]
    return {'random_posts': random_posts}
