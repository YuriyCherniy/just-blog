from django.views.generic import ListView

from posts.models import Post


class IndexView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'core/index.html'
