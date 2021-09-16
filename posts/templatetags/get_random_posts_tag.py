from django import template

from posts.models import Post

register = template.Library()


@register.inclusion_tag('posts/random_posts.html')
def show_posts(current_post_pk):
    '''
    Shows random posts under text of post detail page
    '''
    five_random_posts = Post.objects.order_by('?').exclude(pk=current_post_pk)[:3]
    return {'five_random_posts': five_random_posts}
