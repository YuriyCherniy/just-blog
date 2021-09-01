from django.views.generic import ListView

from posts.models import Post


class IndexView(ListView):
    paginate_by = 5
    template_name = 'core/index.html'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)
